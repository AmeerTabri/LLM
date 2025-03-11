# Document Navigation & Heading Generation Platform

This web application helps navigate through large standard documents and generate missing headings. It is designed to simplify the process of working with extensive documents, particularly when sections are missing headings.

## Features

- **Navigate Through Large Documents**: Easily toggle between different parts of the document.
- **Generate Missing Headings**: Automatically generate titles for sections missing them.
- **Interactive Tree View**: Use an interactive tree structure to explore the document and its sections.
- **Markdown File Integration**: Upload markdown files corresponding to sections and generate headings for them.

## Requirements

Before using the web application, you need to set up the platform either on your local laptop or using Docker containers.

---

## Instructions to Run the Platform on Your Laptop

### Backend Setup

1. **Clone the Repository**: Clone the repository to your local machine.
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. **Install Dependencies**: Install the required Python packages.
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Flask Backend**: Start the Flask backend server.
   ```bash
   flask run
   ```
   The backend will be running at **http://localhost:5000**.

### Frontend Setup

1. **Serve the Frontend**: Navigate to the `treeVisualization` directory and serve the static files using a simple HTTP server.
   ```bash
   cd treeVisualization
   python -m http.server 8000
   ```
   The frontend will be running at **http://localhost:8000**.

---

## Instructions to Run the Platform in Containers

### Backend + Frontend Setup

1. **Clone the Repository**: Clone the repository to your local machine.
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. **Build and Run the Backend Container**:
   ```bash
   docker build -t visualization-app .
   docker run -p 5000:5000 -p 8000:8000 visualization-app
   ```
   The backend will be running at **http://localhost:5000**.

   
   The frontend will be running at **http://localhost:8000**.



## Web Application Usage

### 1. **Upload Files**
   - Upon first opening the web app, you’ll see two drop zones: one for the **data file** and another for the **markdown file**.
   - The **data file** should be in the same format as the files found in a standard Atlas data directory.

### 2. **Toggle Between Parts**
   - Upload the data file.
   - You can toggle between different parts of the document using the button on the top left.
   - Collapse and expand the nodes to further view the sub-sections.

### 3. **Node Types**
   - The nodes are color-coded:
     - **White text**: Sections that already have titles.
     - **Red text**: Sections that are missing titles.

### 4. **Generate Missing Titles**
   - After uploading the corresponding **markdown file**, you can generate a title for a specific section:
     - Right-click on the node and select **Generate Heading** to generate a title for that specific section.
     - Alternatively, you can generate titles for the entire part by using the **Generate Heading** button at the top right.
   - Generated titles will appear in **green** to differentiate them from the existing ones.

### 5. **Navigate to Content**
   - To view the content of any section, right-click on the node and select **Show Content**. This will open a new tab showing the content for the corresponding section.

---

## Usage Example

### Running the Docker Container
   ```bash
   docker-compose up
   ```


