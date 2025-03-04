# DmNotes: A Dungeon Master Aid Tool

## 📖 Description

**DmNotes** is a powerful aid tool designed for Dungeon Masters (DMs) of **Dungeons & Dragons (D&D)** and other tabletop RPGs. This application helps DMs **categorize, organize, and quickly access** essential game elements such as **Characters, Places, Events, Items, and Sheets**.

With **DmNotes**, Dungeon Masters can efficiently manage their campaign details, ensuring a seamless and immersive storytelling experience.

## Repository Structure

The project is structured as follows:

- **`constants.py`** - Initializes directories for local databases.
- **`main.py`** - Sets up the application layout, connects views, and initializes the program.
- **`models.py`** - Defines core data models such as `Character`, `Event`, `Item`, `Place`, and `Sheet`.
- **`utils.py`** - Contains utility functions used across the project.
- **`view.py`** - Defines the general structure and behavior of the views.
- **`character.py`**, `items.py`, `events.py`, `places.py`, `sheets.py` - Define specialized views for their respective data models.

## 🚀 Installation & Setup

To get started with **DmNotes**, follow these steps:

### Clone the repository
```sh
git clone https://github.com/Felifelps/DmNotes.git
```

### Navigate to the project directory
```sh
cd DmNotes
```

### (Optional) Create a virtual environment
It is recommended to create a virtual environment before installing dependencies:
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### Install dependencies
```sh
pip install -r requirements.txt
```

### Run the application
```sh
python main.py
```

## 🎭 Features & Usage

**DmNotes** provides an intuitive way to manage key elements of your RPG campaigns:

- **Characters** - Create and manage characters with attributes like name, race, and class.
- **Events** - Log significant events that shape the storyline.
- **Items** - Create and track in-game items for distribution, trade, or hidden treasures.
- **Places** - Maintain a list of important locations within your world.
- **Sheets** - Store and organize character sheets for quick reference.

## 📌 Requirements

- **Python 3.6 or higher**
- Dependencies listed in `requirements.txt`

## 🤝 Contributing

We welcome contributions! If you want to enhance **DmNotes**, feel free to submit **pull requests**. Bug reports, suggestions, and feature requests are highly appreciated.
