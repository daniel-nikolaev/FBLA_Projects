import os

# Define the folder structure
folders = [
    'idea-2',
    'idea-2/css',
    'idea-2/js',
    'idea-2/images'
]

# Define the HTML content for each page
html_content = {
    'index.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Buford Arena - Go Wolves! Hosting basketball games and community events.">
    <title>Buford Arena - Go Wolves</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/styles.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #009639;">
        <div class="container-fluid">
            <a class="navbar-brand text-white" href="#">Buford Arena</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link text-white" href="calendar.html">Calendar</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="box-office.html">Box Office</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="information.html">Information</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="planner.html">Arena Planner</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="hero text-white text-center py-5" style="background-color: #009639;">
        <h1>Welcome to Buford Arena</h1>
        <p>Go Wolves! Hosting men's and women's basketball games and more!</p>
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
        <p>&copy; 2024 Buford Arena. All rights reserved.</p>
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
    <meta name="description" content="Buford Arena event calendar. See upcoming events.">
    <title>Event Calendar - Buford Arena</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/styles.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #009639;">
        <div class="container-fluid">
            <a class="navbar-brand text-white" href="#">Buford Arena</a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link text-white" href="index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="calendar.html">Calendar</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="box-office.html">Box Office</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="information.html">Information</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="planner.html">Arena Planner</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Calendar Section -->
    <section class="container my-5">
        <h2>Upcoming Events</h2>
        <div class="calendar">
            <div class="row">
                <div class="col-md-4">
                    <div class="event-card">
                        <h5>Men's Basketball Game</h5>
                        <p>Date: December 5, 2024</p>
                        <a href="box-office.html" class="btn btn-success">Buy Tickets</a>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="event-card">
                        <h5>Girls' Basketball Game</h5>
                        <p>Date: December 12, 2024</p>
                        <a href="box-office.html" class="btn btn-success">Buy Tickets</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3">
        <p>&copy; 2024 Buford Arena. All rights reserved.</p>
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
    <meta name="description" content="Buy tickets for events at Buford Arena.">
    <title>Box Office - Buford Arena</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/styles.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #009639;">
        <div class="container-fluid">
            <a class="navbar-brand text-white" href="#">Buford Arena</a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link text-white" href="index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="calendar.html">Calendar</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="box-office.html">Box Office</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="information.html">Information</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="planner.html">Arena Planner</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Ticket Purchase Section -->
    <section class="container my-5">
        <h2>Purchase Tickets</h2>
        <form action="#" method="POST">
            <label for="event">Select Event:</label>
            <select id="event" class="form-control" required>
                <option value="mens_basketball">Men's Basketball Game</option>
                <option value="womens_basketball">Girls' Basketball Game</option>
            </select>
            <br>
            <label for="ticket-quantity">Number of Tickets:</label>
            <input type="number" id="ticket-quantity" class="form-control" placeholder="Enter number of tickets" required>
            <br>
            <button type="submit" class="btn btn-success">Purchase Tickets</button>
        </form>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3">
        <p>&copy; 2024 Buford Arena. All rights reserved.</p>
    </footer>

    <!-- Bootstrap JS & Optional JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',

    'information.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Buford Arena - Directions, Seating, and Amenities.">
    <title>Information - Buford Arena</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/styles.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #009639;">
        <div class="container-fluid">
            <a class="navbar-brand text-white" href="#">Buford Arena</a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link text-white" href="index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="calendar.html">Calendar</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="box-office.html">Box Office</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="information.html">Information</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="planner.html">Arena Planner</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Information Section -->
    <section class="container my-5">
        <h2>Arena Information</h2>
        <p><strong>Address:</strong> 2795 Sawnee Ave, Buford, GA 30518</p>
        <p><strong>Phone:</strong> (770) 945-5035</p>
        <p><strong>Map:</strong> <a href="https://www.google.com/maps/place/2795+Sawnee+Ave,+Buford,+GA+30518" target="_blank">Click here for directions</a></p>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3">
        <p>&copy; 2024 Buford Arena. All rights reserved.</p>
    </footer>

    <!-- Bootstrap JS & Optional JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',

    'planner.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Buford Arena rental planning information.">
    <title>Arena Planner - Buford Arena</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/styles.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #009639;">
        <div class="container-fluid">
            <a class="navbar-brand text-white" href="#">Buford Arena</a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link text-white" href="index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="calendar.html">Calendar</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="box-office.html">Box Office</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="information.html">Information</a></li>
                    <li class="nav-item"><a class="nav-link text-white" href="planner.html">Arena Planner</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Arena Planner Section -->
    <section class="container my-5">
        <h2>Plan Your Event</h2>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" class="form-control" placeholder="Your Name" required>
            <label for="email">Email:</label>
            <input type="email" id="email" class="form-control" placeholder="Your Email" required>
            <label for="eventDate">Event Date:</label>
            <input type="date" id="eventDate" class="form-control" required>
            <label for="eventType">Event Type:</label>
            <select id="eventType" class="form-control">
                <option>Basketball Game</option>
                <option>Concert</option>
                <option>Trade Show</option>
                <option>Private Event</option>
            </select>
            <label for="attendance">Expected Attendance:</label>
            <input type="number" id="attendance" class="form-control" placeholder="Expected Attendance" required>
            <button type="submit" class="btn btn-success">Submit</button>
        </form>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3">
        <p>&copy; 2024 Buford Arena. All rights reserved.</p>
    </footer>

    <!-- Bootstrap JS & Optional JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''
}

# Create the folder structure
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Write the HTML content to respective files
for filename, content in html_content.items():
    file_path = os.path.join('idea-2', filename)
    with open(file_path, 'w') as f:
        f.write(content)

print("Website files created successfully in 'idea-2' directory!")
