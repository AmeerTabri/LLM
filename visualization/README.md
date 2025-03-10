This web application helps navigate through large standart documents and generate missing headings. It is designed to simplify the process of working with extensive documents, particularly when sections are missing headings.

## Features

- **Navigate Through Large Documents**: Easily toggle between different parts of the document.
- **Generate Missing Headings**: Automatically generate titles for sections missing them.
- **Interactive Tree View**: Use an interactive tree structure to explore the document and its sections.
- **Markdown File Integration**: Upload markdown files corresponding to sections and generate headings for them.

## Requirements

Before using the web application, you need to set up the Docker container.

### Steps to Get Started

1. **Install the Docker Container**:

   - Make sure you have Docker installed on your machine.
   - Build and run the Docker container (instructions provided in the repository).

2. **Open the Web App**:

   - After running the Docker container, access the web application through the provided link.

3. **Upload Files**:

   - Upon first opening the web app, you’ll see two drop zones: one for the **data file** and another for the **markdown file**.
   - The **data file** should be in the same format as the files found in a standard Atlas data directory.

4. **Toggle Between Parts**:

   - Upload the data file.
   - You can toggle between different parts of the document using the button on the top left.
   - You can also collapse and expand the nodes to further view the sub-sections.

5. **Node Types**:

   - The nodes are color-coded:
     - **White text**: Sections that already have titles.
     - **Red text**: Sections that are missing titles.

6. **Generate Missing Titles**:

   - After uploading the corresponding **markdown file**, you can generate a title for a specific section:
   - Right-click on the node and select **Generate Heading** to generate a title for that specific section.
   - Alternatively, you can generate titles for the entire part by using the **Generate Heading** button at the top right.
   - Generated titles will appear in **green** to differentiate them from the existing ones.

7. **Navigate to Content**:
   - To view the content of any section, right-click on the node and select **Show Content**. This will open a new tab showing the content for the corresponding section.

## Usage Example

1. Run the Docker container:

   ```bash
   docker-compose up
   ```
2. Upload Files

- Choose a data file from the `examples` directory and drag it into the **data file drop zone**.
- First, drop the **document** file and then the corresponding **document for testing with a markdown file.md** file to enable the generation of headings.

3. Save Progress
   
- Click **Save File** at the top right to save your progress.
- A new tab will open with the content. Right-click and select **Save As** to save it locally.
- Save the file with the `.md` extension to preserve the markdown format.
- The downloaded **md** file can be used later, with generated headings shown in **green**.

4. Review and Reiterate

- As you work through the document, you can repeat the process by uploading new data and markdown files.
- The tree structure will reflect updates, and newly generated headings will be displayed in **green** to clearly differentiate them from the existing ones.

