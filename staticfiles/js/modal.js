function openModal(campaignId, noteId, name, tagId, imageUrl, description) {
    const modalImg = document.getElementById('modalImage');
    const noImage = document.getElementById('no-image');
    const noteName = document.getElementById('id_name');
    const noteTag = document.getElementById('id_tag');
    const noteDescription = document.getElementById('id_description');
    const deleteNoteButton = document.getElementById('deleteNoteButton');
    const noteForm = document.getElementById('note-form');

    noteName.value = name;
    modalImg.src = imageUrl;
    modalImg.alt = name;
    noteTag.value = tagId;
    noteDescription.value = description;
    deleteNoteButton.href = `/campaign/${campaignId}/notes/${noteId}/delete/`
    noteForm.action = `/campaign/${campaignId}/notes/${noteId}/update/`;

    if (imageUrl) {
        modalImg.classList.remove('d-none');
        noImage.classList.add('d-none');
    } else {
        modalImg.classList.add('d-none');
        noImage.classList.remove('d-none');
    }
}