from nicegui import ui

def create_dashboard():
    # Set page title and styling
    ui.page_title('Learning Dashboard')
    
    # Add custom CSS for styling
    ui.add_head_html('''
        <style>
            .dashboard-container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background: #f8fafc;
                min-height: 100vh;
            }
            .header-section {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 40px;
                border-radius: 12px;
                margin-bottom: 30px;
            }
            .section-card {
                background: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 25px;
            }
            .course-item {
                padding: 15px;
                margin: 10px 0;
                background: #f7f9fc;
                border-left: 4px solid #667eea;
                border-radius: 6px;
            }
            .table-container {
                width: 100%;
                overflow-x: auto;
            }
            .custom-table {
                width: 100%;
                border-collapse: collapse;
            }
            .custom-table th {
                background: #667eea;
                color: white;
                padding: 12px;
                text-align: left;
                font-weight: bold;
            }
            .custom-table td {
                padding: 12px;
                border-bottom: 1px solid #e2e8f0;
            }
            .custom-table tr:hover {
                background: #f7f9fc;
            }
            .announcement-item {
                padding: 15px;
                margin: 10px 0;
                background: #fff9e6;
                border-left: 4px solid #ffc107;
                border-radius: 6px;
            }
        </style>
    ''')
    
    # Main container
    with ui.column().classes('dashboard-container'):
        
        # Header section
        with ui.column().classes('header-section w-full'):
            ui.label('Driving the Future').classes('text-4xl font-bold mb-2')
            ui.label('Learning Dashboard').classes('text-xl opacity-90')
        
        # Two column layout for main content
        with ui.row().classes('w-full gap-6'):
            # Left column - Courses and Announcements
            with ui.column().classes('flex-1'):
                # My Courses section
                with ui.column().classes('section-card'):
                    ui.label('My Courses').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    # Course items
                    courses = [
                        {'name': 'Introduction to Data Science', 'instructor': 'Dr. Emily Carter'},
                        {'name': 'Advanced Calculus', 'instructor': 'Prof. David Lee'},
                        {'name': 'Creative Writing Workshop', 'instructor': 'Ms. Olivia Chen'}
                    ]
                    
                    for course in courses:
                        with ui.column().classes('course-item'):
                            ui.label(course['name']).classes('font-bold text-gray-800')
                            ui.label(f"Instructor: {course['instructor']}").classes('text-gray-600 text-sm')
                
                # Announcements section
                with ui.column().classes('section-card'):
                    ui.label('Announcements').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    announcements = [
                        {
                            'title': 'New Course Materials Available',
                            'description': 'Check out the latest materials for the Data Science course.'
                        },
                        {
                            'title': 'Calculus Study Group Reminder',
                            'description': 'Don\'t forget the study group session tomorrow at 4:00 PM.'
                        }
                    ]
                    
                    for announcement in announcements:
                        with ui.column().classes('announcement-item'):
                            ui.label(announcement['title']).classes('font-bold text-gray-800')
                            ui.label(announcement['description']).classes('text-gray-600 text-sm')
            
            # Right column - Events and Deadlines
            with ui.column().classes('flex-1'):
                # Upcoming Events section
                with ui.column().classes('section-card'):
                    ui.label('Upcoming Events').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    # Events table using NiceGUI components instead of raw HTML
                    with ui.column().classes('table-container'):
                        # Table header
                        with ui.grid(columns=3).classes('custom-table w-full bg-blue-600 text-white rounded-t'):
                            ui.label('Event').classes('font-bold p-3')
                            ui.label('Date').classes('font-bold p-3')
                            ui.label('Time').classes('font-bold p-3')
                        
                        # Table rows
                        events = [
                            {'event': 'Data Science Q&A', 'date': 'July 15, 2024', 'time': '2:00 PM'},
                            {'event': 'Calculus Study Group', 'date': 'July 16, 2024', 'time': '4:00 PM'},
                            {'event': 'Writing Workshop Session 2', 'date': 'July 17, 2024', 'time': '6:00 PM'}
                        ]
                        
                        for event in events:
                            with ui.grid(columns=3).classes('custom-table w-full border-b hover:bg-gray-50'):
                                ui.label(event['event']).classes('p-3')
                                ui.label(event['date']).classes('p-3')
                                ui.label(event['time']).classes('p-3')
                
                # Deadlines section
                with ui.column().classes('section-card'):
                    ui.label('Deadlines').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    # Deadlines table using NiceGUI components
                    with ui.column().classes('table-container'):
                        # Table header
                        with ui.grid(columns=3).classes('custom-table w-full bg-blue-600 text-white rounded-t'):
                            ui.label('Assignment').classes('font-bold p-3')
                            ui.label('Course').classes('font-bold p-3')
                            ui.label('Due Date').classes('font-bold p-3')
                        
                        # Table rows
                        deadlines = [
                            {'assignment': 'Data Science Project', 'course': 'Introduction to Data Science', 'due_date': 'July 20, 2024'},
                            {'assignment': 'Calculus Midterm', 'course': 'Advanced Calculus', 'due_date': 'July 22, 2024'},
                            {'assignment': 'Writing Assignment 1', 'course': 'Creative Writing Workshop', 'due_date': 'July 24, 2024'}
                        ]
                        
                        for deadline in deadlines:
                            with ui.grid(columns=3).classes('custom-table w-full border-b hover:bg-gray-50'):
                                ui.label(deadline['assignment']).classes('p-3')
                                ui.label(deadline['course']).classes('p-3')
                                ui.label(deadline['due_date']).classes('p-3')

# Create the dashboard as the root page
@ui.page('/')
def main():
    create_dashboard()

# Run the app
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Learning Dashboard', port=8080, reload=False)