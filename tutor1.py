from nicegui import ui

class TutorDirectory:
    def __init__(self):
        self.view_mode = "table"  # "table" or "two_column"
    
    def create_tutor_directory(self):
        ui.page_title('Tutor Directory - LMS')
        
        # Main container
        with ui.column().classes('max-w-6xl mx-auto p-6'):
            
            # Header with view toggle
            with ui.row().classes('w-full justify-between items-center mb-6'):
                with ui.column():
                    ui.label('Tutor Directory').classes('text-4xl font-bold text-gray-900 mb-2')
                    ui.label('Find contact information for your course tutors.').classes('text-xl text-gray-600')
                
                # View mode toggle
                with ui.row().classes('items-center gap-4'):
                    ui.label('View:').classes('text-gray-700')
                    with ui.button_group().props('outlined'):
                        ui.button('Table View', on_click=lambda: self.set_view('table')) \
                         .props('flat').classes(self.get_button_class('table'))
                        ui.button('List View', on_click=lambda: self.set_view('two_column')) \
                         .props('flat').classes(self.get_button_class('two_column'))
            
            # Display appropriate view based on mode
            if self.view_mode == "table":
                self.create_table_view()
            else:
                self.create_two_column_view()
    
    def get_button_class(self, mode):
        return 'bg-blue-500 text-white' if self.view_mode == mode else 'text-gray-700'
    
    def set_view(self, mode):
        self.view_mode = mode
        ui.navigate.reload()
    
    def create_table_view(self):
        """Table layout from tutor1.png"""
        # Course: Introduction to Programming
        with ui.card().classes('w-full p-6 mb-8'):
            ui.label('Course: Introduction to Programming').classes('text-2xl font-bold text-gray-800 mb-6')
            
            # Tutors table
            with ui.column().classes('w-full'):
                # Table header
                with ui.grid(columns=2).classes('w-full bg-blue-600 text-white rounded-t-lg font-bold'):
                    ui.label('TUTOR').classes('p-4')
                    ui.label('CONTACT').classes('p-4')
                
                # First tutor row
                with ui.grid(columns=2).classes('w-full border-b'):
                    with ui.column().classes('p-4'):
                        ui.label('Dr. Emily Carter').classes('font-semibold text-gray-800')
                        ui.label('e.carter@university.edu').classes('text-gray-600 text-sm')
                    with ui.column().classes('p-4 flex items-center'):
                        ui.button('Copy Email', on_click=lambda: self.copy_email('e.carter@university.edu'), 
                                 icon='content_copy').props('outlined dense').classes('bg-blue-500 text-white')
                
                # Second tutor row
                with ui.grid(columns=2).classes('w-full border-b'):
                    with ui.column().classes('p-4'):
                        ui.label('Prof. David Lee').classes('font-semibold text-gray-800')
                        ui.label('d.lee@university.edu').classes('text-gray-600 text-sm')
                    with ui.column().classes('p-4 flex items-center'):
                        ui.button('Copy Email', on_click=lambda: self.copy_email('d.lee@university.edu'), 
                                 icon='content_copy').props('outlined dense').classes('bg-blue-500 text-white')
        
        # Course: Advanced Calculus
        with ui.card().classes('w-full p-6'):
            ui.label('Course: Advanced Calculus').classes('text-2xl font-bold text-gray-800 mb-6')
            
            # Tutors table
            with ui.column().classes('w-full'):
                # Table header
                with ui.grid(columns=2).classes('w-full bg-green-600 text-white rounded-t-lg font-bold'):
                    ui.label('TUTOR').classes('p-4')
                    ui.label('CONTACT').classes('p-4')
                
                # Tutor row
                with ui.grid(columns=2).classes('w-full border-b'):
                    with ui.column().classes('p-4'):
                        ui.label('Dr. Sarah Chen').classes('font-semibold text-gray-800')
                        ui.label('s.chen@university.edu').classes('text-gray-600 text-sm')
                    with ui.column().classes('p-4 flex items-center'):
                        ui.button('Copy Email', on_click=lambda: self.copy_email('s.chen@university.edu'), 
                                 icon='content_copy').props('outlined dense').classes('bg-green-500 text-white')
    
    def create_two_column_view(self):
        """Two-column layout from tutor2.png"""
        # Course: Introduction to Programming
        with ui.card().classes('w-full p-6 mb-8'):
            ui.label('Course: Introduction to Programming').classes('text-2xl font-bold text-gray-800 mb-6')
            
            # Two column layout for TUTOR and CONTACT
            with ui.grid(columns=2).classes('w-full gap-8'):
                # TUTOR Column
                with ui.column().classes('flex-1'):
                    ui.label('TUTOR').classes('text-lg font-bold text-gray-800 mb-4')
                    
                    # Tutor 1
                    with ui.column().classes('mb-4'):
                        ui.label('Dr. Emily Carter').classes('font-semibold text-gray-800')
                        ui.label('e.carter@university.edu').classes('text-gray-600 text-sm')
                    
                    # Tutor 2
                    with ui.column().classes('mb-4'):
                        ui.label('Prof. David Lee').classes('font-semibold text-gray-800')
                        ui.label('d.lee@university.edu').classes('text-gray-600 text-sm')
                
                # CONTACT Column
                with ui.column().classes('flex-1'):
                    ui.label('CONTACT').classes('text-lg font-bold text-gray-800 mb-4')
                    
                    # Copy Email buttons
                    with ui.column().classes('space-y-4'):
                        ui.button('Copy Email', on_click=lambda: self.copy_email('e.carter@university.edu'), 
                                 icon='content_copy').props('outlined').classes('bg-blue-500 text-white w-full')
                        ui.button('Copy Email', on_click=lambda: self.copy_email('d.lee@university.edu'), 
                                 icon='content_copy').props('outlined').classes('bg-blue-500 text-white w-full')
        
        # Course: Advanced Calculus
        with ui.card().classes('w-full p-6'):
            ui.label('Course: Advanced Calculus').classes('text-2xl font-bold text-gray-800 mb-6')
            
            # Two column layout for TUTOR and CONTACT
            with ui.grid(columns=2).classes('w-full gap-8'):
                # TUTOR Column
                with ui.column().classes('flex-1'):
                    ui.label('TUTOR').classes('text-lg font-bold text-gray-800 mb-4')
                    
                    # Tutor
                    with ui.column().classes('mb-4'):
                        ui.label('Dr. Sarah Chen').classes('font-semibold text-gray-800')
                        ui.label('s.chen@university.edu').classes('text-gray-600 text-sm')
                
                # CONTACT Column
                with ui.column().classes('flex-1'):
                    ui.label('CONTACT').classes('text-lg font-bold text-gray-800 mb-4')
                    
                    # Copy Email button
                    ui.button('Copy Email', on_click=lambda: self.copy_email('s.chen@university.edu'), 
                             icon='content_copy').props('outlined').classes('bg-green-500 text-white w-full')
    
    def copy_email(self, email):
        ui.notify(f'Email copied to clipboard: {email}', type='positive')

# Create and run the app
tutor_app = TutorDirectory()

@ui.page('/')
def main():
    tutor_app.create_tutor_directory()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Tutor Directory', port=8080, reload=False)