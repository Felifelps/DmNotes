import os
import shutil
import flet as ft
from constants import UPLOAD_DIR
from view import View
from utils import get_model_fields


os.makedirs(UPLOAD_DIR, exist_ok=True)


class ModelView(View):
    model = None
    model_help_text = "Model"
    image_field = None

    def __init__(self, page, **kwargs):
        self.fields = get_model_fields(self.model)
        self.fields.pop('id')
        self.identify_field = tuple(self.fields)[0]

        super().__init__(page, **kwargs)

        self.file_picker = ft.FilePicker(on_result=self.on_file_selected)
        self._page.overlay.append(self.file_picker)

        self.model_form_dialog = self.create_model_form_dialog()
        self.delete_model_dialog = self.create_delete_model_dialog()

    def render(self):
        self.search_input = ft.TextField(
            label=f'Pesquisar {self.model_help_text}',
            suffix_icon=ft.Icons.SEARCH,
            on_change=lambda _: self.load_models()
        )

        self.not_found = ft.ResponsiveRow(
            controls=[ft.Text(
                f"Nenhum {self.model_help_text} encontrado :(",
                text_align=ft.TextAlign.CENTER
            )],
            visible=False,
        )

        self.model_list = ft.ListView(expand=True, spacing=10)

        self.load_models()

        self.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            on_click=lambda _: self.open_model_form_dialog()
        )

        self.controls.extend([
            self.search_input,
            self.not_found,
            self.model_list,
        ])

    def load_models(self):
        self.model_list.controls.clear()
        for model in self.model.select().order_by(self.fields[self.identify_field]):
            identify_field = getattr(model, self.identify_field)

            if self.search_input.value.lower() not in identify_field.lower():
                continue

            self.model_list.controls.append(
                ft.Container(
                    on_click=lambda _, m=model: self.open_model_form_dialog(m),
                    key=identify_field,
                    ink=True,
                    content=ft.Row(
                        controls=[
                            ft.Text(identify_field, expand=True),
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                on_click=lambda _, m=model: self.open_delete_model_dialog(
                                    m),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    padding=10,
                    border_radius=10,
                    border=ft.border.all(width=1, color=ft.Colors.PRIMARY),
                )
            )

        self.not_found.visible = not len(self.model_list.controls)

        self._page.update()

    def create_model_form_dialog(self):
        self.inputs = {field_name: ft.TextField(
            label=field.help_text,
            multiline='Text' in str(type(field)),
            visible=field_name != self.image_field,
        ) for field_name, field in self.fields.items()}

        if self.image_field:
            self.image_display = ft.Image(
                src="",
                fit=ft.ImageFit.CONTAIN,
            )
            upload_button = ft.TextButton(
                "Selecionar Imagem", on_click=lambda _: self.file_picker.pick_files(allow_multiple=False))

        def close_dialog(e):
            self._page.close(self.model_form_dialog)

        def save_model(e):
            values = {name: input.value for name, input in self.inputs.items()}

            if getattr(self, 'current_model_id', None):
                query = self.model.update(**values).where(
                    self.model.id == self.current_model_id
                )
                query.execute()
            else:
                self.model.create(**values)

            self.clear_inputs()

            self.load_models()
            close_dialog(e)

            self.message("Criação bem sucedida!")

        dialog_content = ft.ResponsiveRow(
            width=1000,
            controls=list(self.inputs.values())
        )

        if self.image_field:
            dialog_content.controls.extend([
                ft.Container(
                    ink=True,
                    content=self.image_display,
                    on_click=lambda _: os.system(f"explorer {self.image_display.src}")
                ),
                upload_button,
            ])

        return ft.AlertDialog(
            modal=True,
            scrollable=True,
            title=ft.Text(f"Novo {self.model_help_text}", size=20,
                          weight=ft.FontWeight.BOLD),
            content=dialog_content,
            actions=[
                ft.TextButton("Cancelar", on_click=close_dialog),
                ft.TextButton("Salvar", on_click=save_model),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda _: self.clear_inputs()
        )

    def create_delete_model_dialog(self):
        def close_dialog(e):
            self._page.close(self.delete_model_dialog)

        def delete_model(e):
            if getattr(self, 'current_model_id', None):
                self.model.get_by_id(self.current_model_id).delete_instance()
                self.load_models()
            close_dialog(e)

        return ft.AlertDialog(
            modal=True,
            title=ft.Text(f"Deletar {self.model_help_text}", size=20,
                          weight=ft.FontWeight.BOLD),
            content=ft.Text(),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dialog),
                ft.TextButton("Deletar", on_click=delete_model),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda _: self.clear_inputs()
        )

    def open_delete_model_dialog(self, model):
        self.current_model_id = model.id
        self.delete_model_dialog.content.value = f"Realmente deseja deletar {getattr(model, self.identify_field)}?"
        self._page.open(self.delete_model_dialog)

    def open_model_form_dialog(self, model=None):
        action = "Novo" if not model else "Editar"
        self.model_form_dialog.title.value = f"{action} {self.model_help_text}"

        self.current_model_id = None
        if model:
            self.current_model_id = model.id
            data = get_model_fields(model)

            for field, value in data.items():
                self.inputs[field].value = value

            if self.image_field:
                self.image_display.src = getattr(model, self.image_field)

        self._page.open(self.model_form_dialog)

    def clear_inputs(self):
        for input in self.inputs.values():
            input.value = ""

        if self.image_field:
            self.image_display.src = ""

    def on_file_selected(self, e: ft.FilePickerResultEvent):
        if e.files:
            file = e.files[0]

            destination = os.path.join(UPLOAD_DIR, file.name)

            if not os.path.exists(destination):
                shutil.copy(file.path, destination)

            self.inputs[self.image_field].value = destination
            self.selected_image_path = destination
            self.image_display.src = destination
            self._page.update()
