from nicegui import ui
from datetime import datetime

def create_attendance_page():
    ui.page_title('Attendance - LMS')
    
    # Main container
    with ui.column().classes('max-w-4xl mx-auto p-6'):
        
        # Header
        ui.label('Attendance').classes('text-4xl font-bold text-gray-900 mb-2')
        ui.label('Course: Introduction to Programming').classes('text-xl text-gray-600 mb-8')
        
        # Two column layout
        with ui.row().classes('w-full gap-8'):
            # Left column - Attendance Record
            with ui.column().classes('flex-1'):
                with ui.card().classes('w-full p-6'):
                    ui.label('Attendance Record').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    # Attendance table
                    with ui.column().classes('w-full'):
                        # Table header
                        with ui.grid(columns=3).classes('w-full bg-blue-600 text-white rounded-t-lg font-bold'):
                            ui.label('Date').classes('p-3')
                            ui.label('Time').classes('p-3')
                            ui.label('Status').classes('p-3')
                        
                        # Table rows
                        attendance_data = [
                            {'date': '2024-03-15', 'time': '09:00 AM', 'status': 'Present'},
                            {'date': '2024-03-22', 'time': '09:00 AM', 'status': 'Present'},
                            {'date': '2024-03-29', 'time': '09:00 AM', 'status': 'Present'},
                            {'date': '2024-04-05', 'time': '09:00 AM', 'status': 'Present'},
                            {'date': '2024-04-12', 'time': '09:00 AM', 'status': 'Present'}
                        ]
                        
                        for record in attendance_data:
                            with ui.grid(columns=3).classes('w-full border-b hover:bg-gray-50'):
                                ui.label(record['date']).classes('p-3')
                                ui.label(record['time']).classes('p-3')
                                with ui.column().classes('p-3'):
                                    ui.label(record['status']).classes('bg-green-100 text-green-800 px-2 py-1 rounded-full text-sm font-medium')
            
            # Right column - Actions
            with ui.column().classes('flex-1'):
                # Check-In Section
                with ui.card().classes('w-full p-6 mb-6'):
                    ui.label('Check-In').classes('text-2xl font-bold text-gray-800 mb-4')
                    ui.label('Check in to mark your attendance for today\'s session.').classes('text-gray-600 mb-6')
                    
                    # Current date and time display
                    current_time = datetime.now().strftime('%Y-%m-%d %I:%M %p')
                    ui.label(f'Current time: {current_time}').classes('text-sm text-gray-500 mb-4')
                    
                    # Check-in button
                    def handle_check_in():
                        ui.notify('Attendance checked in successfully!', type='positive')
                        
                    ui.button('Check In', on_click=handle_check_in, icon='check_circle') \
                     .classes('w-full bg-green-600 hover:bg-green-700 text-white font-bold py-3 text-lg')
                
                # Tutor Verification Section
                with ui.card().classes('w-full p-6'):
                    ui.label('Tutor Verification').classes('text-2xl font-bold text-gray-800 mb-4')
                    ui.label('Verify student attendance using facial recognition.').classes('text-gray-600 mb-6')
                    
                    # Camera preview placeholder
                    with ui.card().classes('w-full h-48 bg-gray-100 flex items-center justify-center mb-4'):
                        ui.icon('camera_alt').classes('text-4xl text-gray-400')
                        ui.label('Camera Preview').classes('text-gray-500')
                    
                    # Verification button
                    def handle_verification():
                        ui.notify('Attendance verified using facial recognition!', type='positive')
                        
                    ui.button('Verify Attendance', on_click=handle_verification, icon='face') \
                     .classes('w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 text-lg')

# Create the attendance page as root
@ui.page('/')
def main():
    create_attendance_page()

# Run the app
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Attendance System', port=8080, reload=False)