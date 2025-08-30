import datetime

# ------------------ Global Data ------------------
users = {}  # username: password
posts = []  # list of post dictionaries

# ------------------ Functions ------------------

def register_user():
    """Register a new user with username and password."""
    while True:
        username = input("Enter new username: ").strip()
        if username == "":
            print("Username cannot be blank!")
            continue
        if username in users:
            print("Username already exists! Try another.")
            continue
        password = input("Enter password: ").strip()
        if password == "":
            print("Password cannot be blank!")
            continue
        users[username] = password
        print(f"User '{username}' registered successfully!")
        return username

def login_user():
    """Login an existing user."""
    for attempt in range(3):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if username in users and users[username] == password:
            print(f"Welcome, {username}!")
            return username
        else:
            print("Invalid username or password. Try again.")
    print("Too many failed attempts!")
    return None

def create_post(username):
    """Create a new post for the logged-in user."""
    title = input("Enter Post Title: ").strip()
    description = input("Enter Post Description: ").strip()
    if title == "" or description == "":
        print("Title and Description cannot be empty!")
        return
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    post = {
        "author": username,
        "title": title,
        "description": description,
        "date": date
    }
    posts.append(post)
    print("Post created successfully!")

def view_all_posts():
    """Display all posts."""
    if not posts:
        print("\nNo posts available.\n")
        return
    print("\n--- All Posts ---")
    for post in posts:
        print(f"Author: {post['author']}")
        print(f"Title: {post['title']}")
        print(f"Date: {post['date']}")
        print(f"Description: {post['description']}")
        print("-" * 40)

def search_by_username():
    """Search posts by specific username."""
    name = input("Enter username to search: ").strip()
    found = False
    for post in posts:
        if post['author'] == name:
            if not found:
                print(f"\n--- Posts by {name} ---")
            print(f"Title: {post['title']}")
            print(f"Date: {post['date']}")
            print(f"Description: {post['description']}")
            print("-" * 40)
            found = True
    if not found:
        print(f"No posts found for user '{name}'.")

# ------------------ Main Program ------------------

def main():
    print("===== Welcome to PostBoard =====")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = register_user()
            user_menu(username)
        elif choice == "2":
            username = login_user()
            if username:
                user_menu(username)
        elif choice == "3":
            print("Thank you for using PostBoard!")
            break
        else:
            print("Invalid choice! Please try again.")

def user_menu(username):
    """Menu after login."""
    while True:
        print(f"\nWelcome {username}! Choose an option:")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Search Posts by Username")
        print("4. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_post(username)
        elif choice == "2":
            view_all_posts()
        elif choice == "3":
            search_by_username()
        elif choice == "4":
            print(f"Logged out {username}.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
