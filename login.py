from nicegui import ui

def create_login_page():
    # Page configuration
    ui.page_title('Login Page')
    
    # Main container with styling
    with ui.column().classes('w-full max-w-md mx-auto mt-20 p-8 bg-white rounded-lg shadow-lg'):
        # Welcome section
        ui.label('Welcome Back').classes('text-2xl font-bold text-center mb-2')
        ui.label('Sign in to continue to your learning dashboard.').classes('text-gray-600 text-center mb-8')
        
        # Username field
        ui.label('Username').classes('text-sm font-medium')
        username = ui.input(placeholder='Enter your username').props('outlined').classes('w-full mb-4')
        
        # Password field
        ui.label('Password').classes('text-sm font-medium')
        password = ui.input(placeholder='Enter your password', password=True).props('outlined').classes('w-full mb-2')
        
        # Forgot password link
        with ui.row().classes('w-full justify-end mb-6'):
            ui.link('Forgot your password?', '#').classes('text-blue-600 text-sm')
        
        # Login button
        ui.button('Log in', on_click=lambda: login(username.value, password.value)) \
          .classes('w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 mb-6')
        
        # Sign up section
        with ui.row().classes('w-full justify-center'):
            ui.label("Don't have an account?").classes('text-gray-600')
            ui.link('Sign up', '#').classes('text-blue-600 ml-1')

def login(username: str, password: str):
    """Handle login logic"""
    if username and password:
        ui.notify(f'Welcome back, {username}!', type='positive')
        # Here you would typically validate credentials and redirect
    else:
        ui.notify('Please enter both username and password', type='warning')

# Create the page
@ui.page('/')
def main():
    create_login_page()

# Run the app
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Login Page', port=8080, reload=False)