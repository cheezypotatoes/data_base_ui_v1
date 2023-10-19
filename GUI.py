import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFormLayout, QLineEdit, QPushButton, QTableWidget, \
    QRadioButton, QGridLayout, QLabel, QTableWidgetItem
from PyQt6.QtCore import Qt
from default_sql_get_all import check_data
from data_insertion import insert_person_data
from sort_database import sort_data
from delete_data import deleting_data

# TODO Make the delete button, probably delete all "this selected radio button" also add a textbox first for it



class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window/central widget stuff
        self.setWindowTitle("Database UI")
        self.resize(1024, 768)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Class variable that records all line edit made
        self.input_boxes = {}

        # Selected radio buttons
        self.selected_radio = None

        # Creates the form
        self.create_form()

        # Creates the table
        self.create_table()

        # Show every data before the gui shows up
        self.default_show_every_data()

        # Creates the radio buttons
        self.create_radio_buttons()

        # Sort and Delete
        self.sort_and_delete_buttons()

    def default_show_every_data(self):
        """
        Responsible for showing every data inside the database
        first clears the data and grab the data from check_data function
        """
        # Get the data
        self.data = check_data()

        # Clear existing data in the table
        self.table_widget.setRowCount(0)

        # Iterate through the data and add it to the table
        for row_data in self.data:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)

            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row_position, col, item)

    def create_form(self):
        """
        Creates the form layout for the input boxes and store them all in the
        input box so that the insert person data method can reach it
        """
        # List of every requirement
        self.labels = ["First Name", "Last Name", "Gender", "Age", "Birth Date", "Precinct Number",
                       "Sector", "Organization", "Civil Status", "House number"]
        # Form layout
        self.form_layout = QFormLayout(self.central_widget)

        # Make a form for each label
        for label in self.labels:
            input_box_widget = QLineEdit()
            self.form_layout.addRow(label, input_box_widget)
            self.input_boxes[label] = input_box_widget

        # Make the insert data button to the same form layout
        self.insert_data_button = QPushButton("Insert Data")
        self.form_layout.addRow(self.insert_data_button)
        self.insert_data_button.clicked.connect(self.get_data_and_insert)

    def create_table(self):
        """
        Creates the table layout for the table to be made and insert the
        headers and the length of the columns
        """
        # Add a QTableWidget for displaying data
        self.table_widget = QTableWidget()
        self.form_layout.addRow(self.table_widget)

        # Configure the table widget
        self.table_widget.setColumnCount(len(self.labels))
        self.table_widget.setHorizontalHeaderLabels(self.labels)

        # Enable both horizontal and vertical scrollbars
        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

    def get_data_and_insert(self):
        """
        Get the input stuff in the input box dictionary and use it to put it as
        arguments to the insert person data
        """
        # Create individual variables to store the input values
        first_name = self.input_boxes["First Name"].text()
        last_name = self.input_boxes["Last Name"].text()
        gender = self.input_boxes["Gender"].text()
        age = self.input_boxes["Age"].text()
        birth_date = self.input_boxes["Birth Date"].text()
        precinct_number = self.input_boxes["Precinct Number"].text()
        sector = self.input_boxes["Sector"].text()
        organization = self.input_boxes["Organization"].text()
        civil_status = self.input_boxes["Civil Status"].text()
        house_number = self.input_boxes["House number"].text()

        # Insert data from database by using a function from other module
        insert_person_data(first_name,
                           last_name,
                           gender,
                           age,
                           birth_date,
                           precinct_number,
                           sector,
                           organization,
                           civil_status,
                           house_number)

        # Clear all labels after inserting
        for label in self.labels:
            self.input_boxes[label].clear()

        # Refresh the table
        self.default_show_every_data()

    def create_radio_buttons(self):
        """
        This creates the radio button and put it to the list so that I can record it
        and access for later
        """

        # Label for filter and delete
        label = QLabel("Select By: ")
        self.form_layout.addRow(label)

        # Create the radio button list
        self.radio_button_list = []

        # Layout for radio button
        self.radio_layout = QGridLayout()

        self.data_base_names = ["first_name", "last_name", "gender", "age", "birth_date", "precinct_number", "sector",
                           "organization", "civil_status", "house_number"]

        # Place each radio button in 3x3 sine and use label names
        for index, label in enumerate(self.data_base_names):
            radio_button = QRadioButton(label)
            row = index // 3  # Calculate the row based on the index
            col = index % 3  # Calculate the column based on the index
            self.radio_layout.addWidget(radio_button, row, col)
            self.radio_button_list.append(radio_button)  # Add to the list

        # Place the radio layout ot the form layout in a new row
        self.form_layout.addRow(self.radio_layout)

    def sort_and_delete_buttons(self):
        """
        Creates the sort and delete buttons
        """
        # Sort button
        self.sort_button = QPushButton("Sort By")
        self.form_layout.addRow(self.sort_button)
        self.sort_button.clicked.connect(self.sorting_data)

        # Input box for delete
        self.delete_input_box = QLineEdit()
        self.form_layout.addRow("Delete data with: ", self.delete_input_box)

        # Delete button
        self.delete_button = QPushButton("Delete By")
        self.form_layout.addRow(self.delete_button)
        self.delete_button.clicked.connect(self.delete_data)

    def get_selected_radio_button(self):
        """
        Returns the selected radio button
        """
        for radio_button in self.radio_button_list:
            if radio_button.isChecked():
                self.selected_radio = radio_button.text()

    def sorting_data(self):
        """
        Sort the data with the help of the sort_data function and change the table
        """

        # Get the latest selected radio button
        self.get_selected_radio_button()

        # Get the key of selected radio button
        key = self.selected_radio

        # If the key is not None
        if key is not None:
            sorted_list = sort_data(key)

            # Clear existing data in the table
            self.table_widget.setRowCount(0)

            # Iterate through the data and add it to the table
            for row_data in sorted_list:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)

                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table_widget.setItem(row_position, col, item)

    def delete_data(self):
        # Get the latest selected radio button
        self.get_selected_radio_button()

        # Get the key of selected radio button
        key = self.selected_radio

        selected_input = self.delete_input_box.text()

        deleting_data(selected_input, key)

        self.delete_input_box.clear()

        self.default_show_every_data()


def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

