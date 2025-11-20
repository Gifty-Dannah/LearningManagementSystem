from nicegui import ui

@ui.page('/')
def course_management():
    # Set page title
    ui.page_title('Introduction to Data Science - Course Management')
    
    # Main container
    with ui.column().classes('max-w-4xl mx-auto p-8'):
        
        # Course Header
        with ui.column().classes('w-full mb-8'):
            ui.label('Introduction to Data Science').classes('text-4xl font-bold text-gray-900 mb-4')
            ui.label('Learn the fundamentals of data science, including data analysis, visualization, and machine learning techniques.').classes('text-lg text-gray-700')
        
        # Divider
        ui.html('<hr class="border-gray-300 my-8">')
        
        # Course Overview Section
        ui.label('Course Overview').classes('text-2xl font-bold text-gray-800 mb-4')
        overview_text = "This course provides a comprehensive introduction to data science, covering essential concepts and practical skills. You'll learn how to collect, clean, analyze, and visualize data, as well as build predictive models using machine learning algorithms. The course is designed for beginners with no prior experience in data science, but a basic understanding of programming is recommended."
        ui.label(overview_text).classes('text-gray-700 text-lg mb-8')
        
        # Divider
        ui.html('<hr class="border-gray-300 my-8">')
        
        # Course Content Section
        ui.label('Course Content').classes('text-2xl font-bold text-gray-800 mb-6')
        
        # Modules with checkboxes
        modules = [
            'Module 1: Introduction to Data Science',
            'Module 2: Data Analysis and Visualization', 
            'Module 3: Machine Learning Fundamentals',
            'Module 4: Advanced Topics in Data Science'
        ]
        
        for module in modules:
            with ui.row().classes('w-full items-center py-3'):
                ui.checkbox('')
                ui.label(module).classes('text-lg ml-3')
        
        # Divider
        ui.html('<hr class="border-gray-300 my-8">')
        
        # Instructor Section
        ui.label('Instructor').classes('text-2xl font-bold text-gray-800 mb-4')
        with ui.card().classes('bg-blue-50 p-6 w-full'):
            ui.label('Dr. Amelia Chen').classes('text-xl font-bold')
            ui.label('Data Science Expert').classes('text-gray-700')

# Run the app
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Course Management', port=8080)