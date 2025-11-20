from nicegui import ui
from datetime import datetime, timedelta

def create_calendar_page():
    ui.page_title('Calendar - LMS')
    
    # Main container
    with ui.column().classes('max-w-6xl mx-auto p-6'):
        
        # Header
        ui.label('Calendar').classes('text-4xl font-bold text-gray-900 mb-8')
        
        # Two column layout
        with ui.row().classes('w-full gap-8'):
            # Left column - Calendar and Reminders
            with ui.column().classes('flex-1'):
                
                # August 2024 Calendar
                with ui.card().classes('w-full p-6 mb-6'):
                    ui.label('August 2024').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    # Calendar header - days of week
                    days = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
                    with ui.grid(columns=7).classes('w-full text-center mb-2'):
                        for day in days:
                            ui.label(day).classes('font-bold text-gray-600')
                    
                    # Calendar dates for August
                    august_dates = [
                        ['', '', '', '', '1', '2', '3'],
                        ['1', '2', '3', '4', '5', '6', '7'],
                        ['8', '9', '10', '11', '12', '13', '14'],
                        ['15', '16', '17', '18', '19', '20', '21'],
                        ['22', '23', '24', '25', '26', '27', '28'],
                        ['29', '30', '31', '', '', '', '']
                    ]
                    
                    for week in august_dates:
                        with ui.grid(columns=7).classes('w-full text-center'):
                            for date in week:
                                if date:
                                    ui.label(date).classes('p-2 border rounded hover:bg-blue-50 cursor-pointer')
                                else:
                                    ui.label('').classes('p-2')
                
                # September 2024 Calendar
                with ui.card().classes('w-full p-6 mb-6'):
                    ui.label('September 2024').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    # Calendar header - days of week
                    with ui.grid(columns=7).classes('w-full text-center mb-2'):
                        for day in days:
                            ui.label(day).classes('font-bold text-gray-600')
                    
                    # Calendar dates for September
                    september_dates = [
                        ['1', '2', '3', '4', '5', '6', '7'],
                        ['8', '9', '10', '11', '12', '13', '14'],
                        ['15', '16', '17', '18', '19', '20', '21'],
                        ['22', '23', '24', '25', '26', '27', '28'],
                        ['29', '30', '', '', '', '', '']
                    ]
                    
                    for week in september_dates:
                        with ui.grid(columns=7).classes('w-full text-center'):
                            for date in week:
                                if date:
                                    ui.label(date).classes('p-2 border rounded hover:bg-blue-50 cursor-pointer')
                                else:
                                    ui.label('').classes('p-2')
                
                # Reminders Section
                with ui.card().classes('w-full p-6'):
                    ui.label('Reminders').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    reminders = [
                        'Submit Math Assignment',
                        'Read Chapter 3 of History', 
                        'Prepare for English Presentation'
                    ]
                    
                    for reminder in reminders:
                        with ui.row().classes('w-full items-center py-2'):
                            ui.checkbox('')
                            ui.label(reminder).classes('text-gray-700 ml-2')
            
            # Right column - Upcoming Events
            with ui.column().classes('flex-1'):
                with ui.card().classes('w-full p-6'):
                    ui.label('Upcoming').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    events = [
                        {
                            'title': 'Math 101: Calculus Review',
                            'time': '10:00 AM - 11:00 AM',
                            'color': 'blue'
                        },
                        {
                            'title': 'History 202: Ancient Civilizations', 
                            'time': '1:00 PM - 2:00 PM',
                            'color': 'green'
                        },
                        {
                            'title': 'English 301: Shakespearean Literature',
                            'time': '3:00 PM - 4:00 PM',
                            'color': 'purple'
                        }
                    ]
                    
                    for event in events:
                        with ui.card().classes(f'w-full p-4 mb-4 border-l-4 border-{event["color"]}-500'):
                            with ui.column().classes('w-full'):
                                ui.label(event['title']).classes('font-bold text-gray-800 text-lg')
                                ui.label(event['time']).classes('text-gray-600')

# Create the calendar page as root
@ui.page('/')
def main():
    create_calendar_page()

# Run the app
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Calendar', port=8080, reload=False)