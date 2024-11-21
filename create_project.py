import os

# Define the folder and file structure
project_root = 'arena-website'
folders = [
    'assets/css',
    'assets/images',  # You can add images in this folder later
    'assets/js',      # You can add JS files here if necessary
]

files = {
    'index.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Community Arena</title>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
    <header>
        <div class="navbar">
            <a href="index.html">Home</a>
            <a href="events.html">Events Calendar</a>
            <a href="box-office.html">Box Office</a>
            <a href="info.html">Arena Info</a>
            <a href="planner.html">Planner</a>
        </div>
    </header>

    <section class="hero">
        <h1>Welcome to the Community Arena</h1>
        <p>Host your next event in our 3,500-seat gymnasium and arena.</p>
    </section>

    <section class="highlights">
        <div class="highlight-box">
            <h2>Upcoming Events</h2>
            <p>See what's coming up in our arena and get your tickets today.</p>
        </div>
        <div class="highlight-box">
            <h2>Book the Arena</h2>
            <p>Plan your event with us – it's easy and affordable.</p>
        </div>
    </section>

    <footer>
        <p>&copy; 2024 Community Arena | All Rights Reserved</p>
    </footer>
</body>
</html>
    ''',

    'events.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Events Calendar - Community Arena</title>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
    <header>
        <div class="navbar">
            <a href="index.html">Home</a>
            <a href="events.html">Events Calendar</a>
            <a href="box-office.html">Box Office</a>
            <a href="info.html">Arena Info</a>
            <a href="planner.html">Planner</a>
        </div>
    </header>

    <section class="events-calendar">
        <h1>Upcoming Events</h1>
        <div class="calendar">
            <ul>
                <li>December 1, 2024 - Local Basketball Game</li>
                <li>December 5, 2024 - Rock Concert</li>
                <li>December 10, 2024 - Trade Show</li>
                <li>December 15, 2024 - High School Graduation</li>
            </ul>
        </div>
    </section>

    <footer>
        <p>&copy; 2024 Community Arena | All Rights Reserved</p>
    </footer>
</body>
</html>
    ''',

    'box-office.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Box Office - Community Arena</title>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
    <header>
        <div class="navbar">
            <a href="index.html">Home</a>
            <a href="events.html">Events Calendar</a>
            <a href="box-office.html">Box Office</a>
            <a href="info.html">Arena Info</a>
            <a href="planner.html">Planner</a>
        </div>
    </header>

    <section class="box-office">
        <h1>Buy Tickets</h1>
        <p>Select an event to purchase tickets:</p>
        <form action="/purchase-tickets" method="POST">
            <label for="event">Choose Event:</label>
            <select name="event" id="event">
                <option value="basketball">Local Basketball Game</option>
                <option value="concert">Rock Concert</option>
                <option value="trade-show">Trade Show</option>
                <option value="graduation">High School Graduation</option>
            </select>

            <label for="tickets">Number of Tickets:</label>
            <input type="number" name="tickets" id="tickets" min="1" max="10" required>

            <button type="submit">Buy Tickets</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2024 Community Arena | All Rights Reserved</p>
    </footer>
</body>
</html>
    ''',

    'info.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arena Information - Community Arena</title>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
    <header>
        <div class="navbar">
            <a href="index.html">Home</a>
            <a href="events.html">Events Calendar</a>
            <a href="box-office.html">Box Office</a>
            <a href="info.html">Arena Info</a>
            <a href="planner.html">Planner</a>
        </div>
    </header>

    <section class="arena-info">
        <h1>Arena Information</h1>
        <div class="info-content">
            <h2>Directions</h2>
            <p>Our arena is located at 123 Arena St., Cityville, Country. Parking is available on-site.</p>

            <h2>Seating Chart</h2>
            <img src="assets/images/seating-chart.jpg" alt="Seating Chart">

            <h2>Policies</h2>
            <p>We have a no-smoking policy inside the arena. No outside food or drinks are allowed.</p>

            <h2>Amenities</h2>
            <ul>
                <li>Accessible seating</li>
                <li>Concessions and snacks</li>
                <li>Free Wi-Fi</li>
            </ul>
        </div>
    </section>

    <footer>
        <p>&copy; 2024 Community Arena | All Rights Reserved</p>
    </footer>
</body>
</html>
    ''',

    'planner.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planner - Community Arena</title>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
    <header>
        <div class="navbar">
            <a href="index.html">Home</a>
            <a href="events.html">Events Calendar</a>
            <a href="box-office.html">Box Office</a>
            <a href="info.html">Arena Info</a>
            <a href="planner.html">Planner</a>
        </div>
    </header>

    <section class="arena-planner">
        <h1>Plan Your Event</h1>
        <p>Interested in hosting an event? Contact us to start planning your rental.</p>

        <h2>Contact Information</h2>
        <p>Email: rentals@arena.com</p>
        <p>Phone: (123) 456-7890</p>

        <h2>Rental Information</h2>
        <p>For pricing and availability, please submit a rental inquiry.</p>
    </section>

    <footer>
        <p>&copy; 2024 Community Arena | All Rights Reserved</p>
    </footer>
</body>
</html>
    ''',

    'assets/css/styles.css': '''body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background-color: #333;
    color: white;
    padding: 10px 0;
    text-align: center;
}

.navbar a {
    color: white;
    margin: 0 15px;
    text-decoration: none;
    text-transform: uppercase;
}

.navbar a:hover {
    text-decoration: underline;
}

.hero {
    background-color: #333;
    color: white;
    padding: 50px 0;
}

.highlights {
    display: flex;
    justify-content: space-around;
    padding: 20px;
}

.highlight-box {
    background-color: #444;
    color: white;
    padding: 20px;
    width: 30%;
    text-align: center;
}
    '''
}

# Function to create the directories and files
def create_project():
    # Create directories
    for folder in folders:
        os.makedirs(os.path.join(project_root, folder), exist_ok=True)
    
    # Create files with content
    for filename, content in files.items():
        file_path = os.path.join(project_root, filename)
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Created: {file_path}")

# Run the function to create the project
if __name__ == "__main__":
    os.makedirs(project_root, exist_ok=True)
    create_project()
