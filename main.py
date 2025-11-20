from nicegui import ui

# ===== SHARED NAVIGATION COMPONENT =====
def create_navigation(current_page=''):
    """Create a navigation bar that appears on all pages except login/signup"""
    with ui.header().classes('bg-teal-800 text-white shadow-lg'):
        with ui.row().classes('w-full max-w-6xl mx-auto items-center justify-between p-4'):
            with ui.row().classes('items-center gap-8'):
                ui.link('Learning Management System', '/dashboard').classes('text-xl font-bold')
                
                with ui.row().classes('gap-4'):
                    ui.link('Dashboard', '/dashboard').classes(f"px-3 py-2 rounded hover:bg-teal-700 {'bg-teal-700' if current_page == 'dashboard' else ''}")
                    ui.link('Courses', '/courses').classes(f"px-3 py-2 rounded hover:bg-teal-700 {'bg-teal-700' if current_page == 'courses' else ''}")
                    ui.link('Calendar', '/calendar').classes(f"px-3 py-2 rounded hover:bg-teal-700 {'bg-teal-700' if current_page == 'calendar' else ''}")
                    ui.link('Attendance', '/attendance').classes(f"px-3 py-2 rounded hover:bg-teal-700 {'bg-teal-700' if current_page == 'attendance' else ''}")
                    ui.link('Tutors', '/tutors').classes(f"px-3 py-2 rounded hover:bg-teal-700 {'bg-teal-700' if current_page == 'tutors' else ''}")
            
            with ui.row().classes('items-center gap-4'):
                ui.button(icon='account_circle').props('flat round color=white')
                ui.link('Logout', '/').classes('px-3 py-2 rounded hover:bg-teal-700')

# ===== LOGIN PAGE =====
@ui.page('/')
def login_page():
    ui.page_title('Login - LMS')
    
    # Remove any background styling for clean login page
    ui.add_head_html('<style>body { background: #f8fafc; }</style>')
    
    with ui.column().classes('w-full max-w-md mx-auto mt-20 p-8 bg-white rounded-lg shadow-lg'):
        ui.label('Welcome Back').classes('text-2xl font-bold text-center mb-2')
        ui.label('Sign in to continue to your learning dashboard.').classes('text-gray-600 text-center mb-8')
        
        ui.label('Username').classes('text-sm font-medium')
        username = ui.input(placeholder='Enter your username').props('outlined').classes('w-full mb-4')
        
        ui.label('Password').classes('text-sm font-medium')
        password = ui.input(placeholder='Enter your password', password=True).props('outlined').classes('w-full mb-2')
        
        with ui.row().classes('w-full justify-end mb-6'):
            ui.link('Forgot your password?', '#').classes('text-teal-600 text-sm')
        
        # Login button that redirects to dashboard
        def handle_login():
            if username.value and password.value:
                ui.navigate.to('/dashboard')
            else:
                ui.notify('Please enter both username and password', type='warning')
                
        ui.button('Log in', on_click=handle_login) \
          .classes('w-full bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 mb-6')
        
        with ui.row().classes('w-full justify-center'):
            ui.label("Don't have an account?").classes('text-gray-600')
            ui.link('Sign up', '/signup').classes('text-teal-600 ml-1 font-medium')

# ===== SIGNUP PAGE =====
@ui.page('/signup')
def signup_page():
    ui.page_title('Sign Up - LMS')
    
    # Remove any background styling for clean signup page
    ui.add_head_html('<style>body { background: #f8fafc; }</style>')
    
    with ui.column().classes('w-full max-w-md mx-auto mt-10 p-8 bg-white rounded-lg shadow-lg'):
        # Back to login link
        with ui.row().classes('w-full mb-4'):
            ui.link('← Back to Login', '/').classes('text-teal-600 text-sm')
        
        ui.label('Create Account').classes('text-2xl font-bold text-center mb-2')
        ui.label('Join our learning community today.').classes('text-gray-600 text-center mb-8')
        
        # Username field
        ui.label('Username *').classes('text-sm font-medium text-gray-700')
        username = ui.input(placeholder='Enter your username').props('outlined').classes('w-full mb-4')
        
        # Email field
        ui.label('Email *').classes('text-sm font-medium text-gray-700')
        email = ui.input(placeholder='Enter your email').props('outlined type=email').classes('w-full mb-4')
        
        # Password field
        ui.label('Password *').classes('text-sm font-medium text-gray-700')
        password = ui.input(placeholder='Create a password', password=True).props('outlined').classes('w-full mb-4')
        
        # Role field
        ui.label('Role').classes('text-sm font-medium text-gray-700')
        role = ui.select(
            options=['Student', 'Instructor', 'Administrator'],
            value='Student'
        ).props('outlined').classes('w-full mb-4')
        
        # Phone field
        ui.label('Phone *').classes('text-sm font-medium text-gray-700')
        phone = ui.input(placeholder='Enter your phone number').props('outlined').classes('w-full mb-4')
        
        # Bio field
        ui.label('Bio *').classes('text-sm font-medium text-gray-700')
        bio = ui.textarea(placeholder='Tell us about yourself...').props('outlined').classes('w-full mb-6')
        
        # Signup button
        def handle_signup():
            # Basic validation
            if not all([username.value, email.value, password.value, phone.value, bio.value]):
                ui.notify('Please fill in all required fields', type='warning')
                return
            
            if '@' not in email.value:
                ui.notify('Please enter a valid email address', type='warning')
                return
            
            # Simulate successful signup
            ui.notify(f'Account created successfully! Welcome {username.value}', type='positive')
            # Redirect to login after 2 seconds
            ui.timer(2.0, lambda: ui.navigate.to('/'), once=True)
        
        ui.button('Create Account', on_click=handle_signup, icon='person_add') \
          .classes('w-full bg-teal-600 hover:bg-teal-700 text-white font-bold py-3 mb-4')
        
        # Already have account link
        with ui.row().classes('w-full justify-center'):
            ui.label('Already have an account?').classes('text-gray-600')
            ui.link('Sign in', '/').classes('text-teal-600 ml-1 font-medium')

# ===== DASHBOARD PAGE =====
@ui.page('/dashboard')
def dashboard_page():
    ui.page_title('Dashboard - LMS')
    create_navigation('dashboard')
    
    # Main container
    with ui.column().classes('w-full max-w-6xl mx-auto p-6'):
        
        # Welcome section
        with ui.column().classes('w-full mb-8'):
            ui.label('Driving the Future').classes('text-4xl font-bold text-gray-900 mb-2')
            ui.label('Learning Dashboard').classes('text-xl text-gray-600')
        
        # Quick actions
        with ui.row().classes('w-full gap-4 mb-8'):
            ui.button('View All Courses', on_click=lambda: ui.navigate.to('/courses')) \
             .classes('bg-teal-600 text-white px-6 py-3 rounded-lg')
            ui.button('Calendar', on_click=lambda: ui.navigate.to('/calendar'), icon='calendar_today') \
             .classes('bg-teal-600 text-white px-6 py-3 rounded-lg')
            ui.button('Attendance', on_click=lambda: ui.navigate.to('/attendance'), icon='check_circle') \
             .classes('bg-teal-600 text-white px-6 py-3 rounded-lg')
            ui.button('Tutor Directory', on_click=lambda: ui.navigate.to('/tutors'), icon='people') \
             .classes('bg-teal-600 text-white px-6 py-3 rounded-lg')
        
        # Two column layout for main content
        with ui.row().classes('w-full gap-6'):
            # Left column - Courses and Announcements
            with ui.column().classes('flex-1'):
                # My Courses section
                with ui.card().classes('w-full p-6'):
                    with ui.column().classes('w-full'):
                        ui.label('My Courses').classes('text-2xl font-bold text-gray-800 mb-4')
                        
                        courses = [
                            {'name': 'Introduction to Data Science', 'instructor': 'Dr. Emily Carter', 'progress': 65},
                            {'name': 'Advanced Calculus', 'instructor': 'Prof. David Lee', 'progress': 40},
                            {'name': 'Creative Writing Workshop', 'instructor': 'Ms. Olivia Chen', 'progress': 80}
                        ]
                        
                        for course in courses:
                            with ui.card().classes('w-full p-4 mb-4 cursor-pointer hover:bg-gray-50') as card:
                                card.on('click', lambda: ui.navigate.to('/courses'))
                                with ui.column().classes('w-full'):
                                    ui.label(course['name']).classes('font-bold text-gray-800')
                                    ui.label(f"Instructor: {course['instructor']}").classes('text-gray-600 text-sm mb-2')
                                    ui.linear_progress(course['progress']/100).classes('w-full')
                                    ui.label(f'{course["progress"]}% complete').classes('text-xs text-gray-500 mt-1')
                
                # Announcements section
                with ui.card().classes('w-full p-6'):
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
                        with ui.card().classes('w-full p-4 mb-4 bg-yellow-50 border-l-4 border-yellow-400'):
                            ui.label(announcement['title']).classes('font-bold text-gray-800')
                            ui.label(announcement['description']).classes('text-gray-600 text-sm')
            
            # Right column - Events and Deadlines
            with ui.column().classes('flex-1'):
                # Upcoming Events section
                with ui.card().classes('w-full p-6'):
                    ui.label('Upcoming Events').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    events = [
                        {'event': 'Data Science Q&A', 'date': 'July 15, 2024', 'time': '2:00 PM'},
                        {'event': 'Calculus Study Group', 'date': 'July 16, 2024', 'time': '4:00 PM'},
                        {'event': 'Writing Workshop Session 2', 'date': 'July 17, 2024', 'time': '6:00 PM'}
                    ]
                    
                    for event in events:
                        with ui.row().classes('w-full justify-between items-center py-3 border-b'):
                            with ui.column():
                                ui.label(event['event']).classes('font-semibold')
                                ui.label(f"{event['date']} at {event['time']}").classes('text-sm text-gray-600')
                            ui.button('Join', icon='video_call').props('outlined dense')
                
                # Deadlines section
                with ui.card().classes('w-full p-6'):
                    ui.label('Deadlines').classes('text-2xl font-bold text-gray-800 mb-4')
                    
                    deadlines = [
                        {'assignment': 'Data Science Project', 'course': 'Introduction to Data Science', 'due_date': 'July 20, 2024'},
                        {'assignment': 'Calculus Midterm', 'course': 'Advanced Calculus', 'due_date': 'July 22, 2024'},
                        {'assignment': 'Writing Assignment 1', 'course': 'Creative Writing Workshop', 'due_date': 'July 24, 2024'}
                    ]
                    
                    for deadline in deadlines:
                        with ui.row().classes('w-full justify-between items-center py-3 border-b'):
                            with ui.column():
                                ui.label(deadline['assignment']).classes('font-semibold')
                                ui.label(deadline['course']).classes('text-sm text-gray-600')
                            ui.label(deadline['due_date']).classes('text-red-600 font-medium')

# ===== COURSES PAGE =====
@ui.page('/courses')
def courses_page():
    ui.page_title('Courses - LMS')
    create_navigation('courses')
    
    # Main container
    with ui.column().classes('w-full max-w-4xl mx-auto p-6'):
        
        # Course Header
        with ui.column().classes('w-full mb-8'):
            ui.label('Introduction to Data Science').classes('text-4xl font-bold text-gray-900 mb-4')
            ui.label('Learn the fundamentals of data science, including data analysis, visualization, and machine learning techniques.').classes('text-lg text-gray-700 leading-relaxed')
        
        # Course actions
        with ui.row().classes('w-full gap-4 mb-8'):
            ui.button('Start Learning', icon='play_arrow').classes('bg-teal-600 text-white px-6 py-3')
            ui.button('Download Materials', icon='download').classes('bg-teal-600 text-white px-6 py-3')
            ui.button('Discussion Forum', icon='forum').classes('bg-teal-600 text-white px-6 py-3')
        
        # Divider line
        ui.html('<hr class="border-t-2 border-gray-300 my-8">')
        
        # Course Overview Section
        ui.label('Course Overview').classes('text-2xl font-bold text-gray-800 mb-4')
        overview_text = """
        This course provides a comprehensive introduction to data science, covering essential concepts and practical skills. 
        You'll learn how to collect, clean, analyze, and visualize data, as well as build predictive models using machine 
        learning algorithms. The course is designed for beginners with no prior experience in data science, but a basic 
        understanding of programming is recommended.
        """
        ui.label(overview_text).classes('text-gray-700 leading-7 text-lg mb-8')
        
        # Divider line
        ui.html('<hr class="border-t-2 border-gray-300 my-8">')
        
        # Course Content Section
        ui.label('Course Content').classes('text-2xl font-bold text-gray-800 mb-6')
        
        # Modules with checkboxes
        modules = [
            {'prefix': 'Module 1', 'title': 'Introduction to Data Science', 'duration': '2 hours', 'completed': True},
            {'prefix': 'Module 2', 'title': 'Data Analysis and Visualization', 'duration': '3 hours', 'completed': False},
            {'prefix': 'Module 3', 'title': 'Machine Learning Fundamentals', 'duration': '4 hours', 'completed': False},
            {'prefix': 'Module 4', 'title': 'Advanced Topics in Data Science', 'duration': '3 hours', 'completed': False}
        ]
        
        for module in modules:
            with ui.card().classes('w-full p-4 mb-4 cursor-pointer hover:bg-gray-50'):
                with ui.row().classes('w-full items-center justify-between'):
                    with ui.row().classes('items-center gap-4'):
                        ui.checkbox('', value=module['completed']).props('color=teal')
                        with ui.column():
                            ui.label(module['prefix']).classes('font-semibold text-gray-900 text-lg')
                            ui.label(module['title']).classes('text-gray-700 -mt-1')
                    with ui.column().classes('text-right'):
                        ui.label(module['duration']).classes('text-sm text-gray-500')
                        ui.button('Start', icon='play_arrow').props('outlined dense') \
                         .classes('bg-teal-500 text-white' if not module['completed'] else 'bg-gray-300')
        
        # Divider line
        ui.html('<hr class="border-t-2 border-gray-300 my-8">')
        
        # Instructor Section
        ui.label('Instructor').classes('text-2xl font-bold text-gray-800 mb-4')
        with ui.card().classes('w-full bg-teal-50 border-l-4 border-teal-500'):
            with ui.row().classes('w-full items-center p-6'):
                ui.icon('account_circle').classes('text-4xl text-teal-600 mr-4')
                with ui.column():
                    ui.label('Dr. Amelia Chen').classes('text-xl font-bold text-gray-900')
                    ui.label('Data Science Expert').classes('text-gray-700')
                    ui.label('10+ years experience in data analytics and machine learning').classes('text-sm text-gray-600 mt-1')

# ===== CALENDAR PAGE =====
@ui.page('/calendar')
def calendar_page():
    ui.page_title('Calendar - LMS')
    create_navigation('calendar')
    
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
                                    ui.label(date).classes('p-2 border rounded hover:bg-teal-50 cursor-pointer')
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
                                    ui.label(date).classes('p-2 border rounded hover:bg-teal-50 cursor-pointer')
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
                            'color': 'teal'
                        },
                        {
                            'title': 'History 202: Ancient Civilizations', 
                            'time': '1:00 PM - 2:00 PM',
                            'color': 'teal'
                        },
                        {
                            'title': 'English 301: Shakespearean Literature',
                            'time': '3:00 PM - 4:00 PM',
                            'color': 'teal'
                        }
                    ]
                    
                    for event in events:
                        with ui.card().classes('w-full p-4 mb-4 border-l-4 border-teal-500'):
                            with ui.column().classes('w-full'):
                                ui.label(event['title']).classes('font-bold text-gray-800 text-lg')
                                ui.label(event['time']).classes('text-gray-600')

# ===== ATTENDANCE PAGE =====
@ui.page('/attendance')
def attendance_page():
    ui.page_title('Attendance - LMS')
    create_navigation('attendance')
    
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
                        with ui.grid(columns=3).classes('w-full bg-teal-600 text-white rounded-t-lg font-bold'):
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
                    
                    # Check-in button
                    def handle_check_in():
                        ui.notify('Attendance checked in successfully!', type='positive')
                        
                    ui.button('Check In', on_click=handle_check_in, icon='check_circle') \
                     .classes('w-full bg-teal-600 hover:bg-teal-700 text-white font-bold py-3 text-lg')
                
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
                     .classes('w-full bg-teal-600 hover:bg-teal-700 text-white font-bold py-3 text-lg')

# ===== TUTORS PAGE =====
@ui.page('/tutors')
def tutors_page():
    ui.page_title('Tutor Directory - LMS')
    create_navigation('tutors')
    
    # Main container
    with ui.column().classes('max-w-4xl mx-auto p-6'):
        
        # Header
        ui.label('Tutor Directory').classes('text-4xl font-bold text-gray-900 mb-4')
        ui.label('Find contact information for your course tutors.').classes('text-xl text-gray-600 mb-8')
        
        # Course: Introduction to Programming
        with ui.card().classes('w-full p-6 mb-8'):
            ui.label('Course: Introduction to Programming').classes('text-2xl font-bold text-gray-800 mb-6')
            
            # Tutors table
            with ui.column().classes('w-full'):
                # Table header
                with ui.grid(columns=2).classes('w-full bg-teal-600 text-white rounded-t-lg font-bold'):
                    ui.label('TUTOR').classes('p-4')
                    ui.label('CONTACT').classes('p-4')
                
                # First tutor row
                with ui.grid(columns=2).classes('w-full border-b'):
                    with ui.column().classes('p-4'):
                        ui.label('Dr. Emily Carter').classes('font-semibold text-gray-800')
                        ui.label('e.carter@university.edu').classes('text-gray-600 text-sm')
                    with ui.column().classes('p-4 flex items-center'):
                        def copy_emily_email():
                            ui.notify('Email copied to clipboard: e.carter@university.edu', type='positive')
                        ui.button('Copy Email', on_click=copy_emily_email, icon='content_copy') \
                         .props('outlined dense').classes('bg-teal-500 text-white')
                
                # Second tutor row
                with ui.grid(columns=2).classes('w-full border-b'):
                    with ui.column().classes('p-4'):
                        ui.label('Prof. David Lee').classes('font-semibold text-gray-800')
                        ui.label('d.lee@university.edu').classes('text-gray-600 text-sm')
                    with ui.column().classes('p-4 flex items-center'):
                        def copy_david_email():
                            ui.notify('Email copied to clipboard: d.lee@university.edu', type='positive')
                        ui.button('Copy Email', on_click=copy_david_email, icon='content_copy') \
                         .props('outlined dense').classes('bg-teal-500 text-white')
        
        # Course: Advanced Calculus
        with ui.card().classes('w-full p-6'):
            ui.label('Course: Advanced Calculus').classes('text-2xl font-bold text-gray-800 mb-6')
            
            # Tutors table
            with ui.column().classes('w-full'):
                # Table header
                with ui.grid(columns=2).classes('w-full bg-teal-600 text-white rounded-t-lg font-bold'):
                    ui.label('TUTOR').classes('p-4')
                    ui.label('CONTACT').classes('p-4')
                
                # Tutor row
                with ui.grid(columns=2).classes('w-full border-b'):
                    with ui.column().classes('p-4'):
                        ui.label('Dr. Sarah Chen').classes('font-semibold text-gray-800')
                        ui.label('s.chen@university.edu').classes('text-gray-600 text-sm')
                    with ui.column().classes('p-4 flex items-center'):
                        def copy_sarah_email():
                            ui.notify('Email copied to clipboard: s.chen@university.edu', type='positive')
                        ui.button('Copy Email', on_click=copy_sarah_email, icon='content_copy') \
                         .props('outlined dense').classes('bg-teal-500 text-white')

# ===== RUN THE APPLICATION =====
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Learning Management System', port=8080, reload=False)