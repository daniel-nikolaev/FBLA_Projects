import os

# Define the folder structure
folders = [
    'website',
    'website/css',
    'website/js',
    'website/images'
]

# Define the HTML content for each page
html_content = {
    'index.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Community Arena for events such as sports, concerts, and trade shows.">
    <title>Community Arena</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/styles.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Community Arena</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="calendar.html">Calendar</a></li>
                    <li class="nav-item"><a class="nav-link" href="box-office.html">Box Office</a></li>
                    <li class="nav-item"><a class="nav-link" href="information.html">Information</a></li>
                    <li class="nav-item"><a class="nav-link" href="planner.html">Arena Planner</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="hero bg-primary text-white text-center py-5">
        <h1>Welcome to the Community Arena</h1>
        <p>Hosting sporting events, concerts, trade shows, and more.</p>
        <a href="calendar.html" class="btn btn-light btn-lg">See Upcoming Events</a>
    </header>

    <!-- Quick Links -->
    <section class="container my-5">
        <div class="row">
            <div class="col-md-4">
                <h2>Upcoming Events</h2>
                <ul>
                    <li><a href="calendar.html">View Full Calendar</a></li>
                    <li><a href="box-office.html">Buy Tickets</a></li>
                </ul>
            </div>
            <div class="col-md-4">
                <h2>Book Your Event</h2>
                <p>Rent the arena for your own event.</p>
                <a href="planner.html" class="btn btn-primary">Plan Your Event</a>
            </div>
            <div class="col-md-4">
                <h2>Venue Information</h2>
                <ul>
                    <li><a href="information.html">Directions & Parking</a></li>
                    <li><a href="information.html">Seating Chart</a></li>
                    <li><a href="information.html">Amenities</a></li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3">
        <p>&copy; 2024 Community Arena. All rights reserved.</p>
        <p>Follow us: 
            <a href="#" class="text-white">Facebook</a> | 
            <a href="#" class="text-white">Instagram</a> | 
            <a href="#" class="text-white">Twitter</a>
        </p>
    </footer>

    <!-- Bootstrap JS & Optional JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',

    'calendar.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Community Arena event calendar. See upcoming events.">
    <title>Event Calendar - Community Arena</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/styles.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Community Arena</a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="calendar.html">Calendar</a></li>
                    <li class="nav-item"><a class="nav-link" href="box-office.html">Box Office</a></li>
                    <li class="nav-item"><a class="nav-link" href="information.html">Information</a></li>
                    <li class="nav-item"><a class="nav-link" href="planner.html">Arena Planner</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Calendar Section -->
    <section class="container my-5">
        <h2>Upcoming Events</h2>
        <div class="calendar">
            <!-- Simple Calendar Grid (Example) -->
            <div class="row">
                <div class="col-md-4">
                    <div class="event-card">
                        <h5>Event Title</h5>
                        <p>Date: December 5, 2024</p>
                        <a href="box-office.html" class="btn btn-primary">Buy Tickets</a>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="event-card">
                        <h5>Event Title</h5>
                        <p>Date: December 12, 2024</p>
                        <a href="box-office.html" class="btn btn-primary">Buy Tickets</a>
                    </div>
                </div>
                <!-- Add more events as necessary -->
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3">
        <p>&copy; 2024 Community Arena. All rights reserved.</p>
    </footer>

    <!-- Bootstrap JS & Optional JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',

    'box-office.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Buy tickets for events at the Community Arena.">
    <title>Box Office - Community Arena</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/styles.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Community Arena</a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="calendar.html">Calendar</a></li>
                    <li class="nav-item"><a class="nav-link" href="box-office.html">Box Office</a></li>
                    <li class="nav-item"><a class="nav-link" href="information.html">Information</a></li>
                    <li class="nav-item"><a class="nav-link" href="planner.html">Arena Planner</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Ticket Purchase Section -->
    <section class="container my-5">
        <h2>Buy Tickets</h2>
        <p>Choose the event and purchase your tickets here.</p>
        <div class="ticket-card">
            <h5>Event Title</h5>
            <p>Date: December 5, 2024</p>
            <form action="purchase-tickets.html" method="post">
                <!-- Add ticket form here -->
                <label for="tickets">Number of Tickets:</label>
                <input type="number" id="tickets" name="tickets" min="1" max="10" value="1" required>
                <button type="submit" class="btn btn-primary">Buy Tickets</button>
            </form>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3">
        <p>&copy; 2024 Community Arena. All rights reserved.</p>
    </footer>

    <!-- Bootstrap JS & Optional JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''
}

# Create folder structure
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create HTML files and write the content
for filename, content in html_content.items():
    with open(f'website/{filename}', 'w') as file:
        file.write(content)

print("Website structure and files have been created!")
