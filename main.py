import streamlit as st
import sqlite3

def create_databases():
    # Create subscribers database
    conn = sqlite3.connect('subscribers.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS subscribers
                 (email TEXT PRIMARY KEY)''')
    conn.commit()
    conn.close()

    # Create reviews database
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reviews
                 (review TEXT PRIMARY KEY)''')
    conn.commit()
    conn.close()

def add_subscriber(email):
    conn = sqlite3.connect('subscribers.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
        conn.commit()
        st.success(f"Thank you for subscribing with {email}!")
    except sqlite3.IntegrityError:
        st.warning(f"{email} is already subscribed.")
    finally:
        conn.close()

def add_review(review):
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO reviews (review) VALUES (?)", (review,))
        conn.commit()
        st.success("Thank you for your review!")
    except sqlite3.IntegrityError:
        st.warning("This review already exists.")
    finally:
        conn.close()

def main():
    st.title("Wealth Watcher")
    commands = {
        "/stockprice": "Get the current stock price for a given ticker symbol (e.g., /stockprice tsla, /stockprice SBIN.BO, /stockprice RELIANCE.NS).",
        "/plot": "Plot a graph for a given stock ticker and date range (e.g., /plot AAPL 2023-01-01 2023-04-30).",
        "/stock": "Get stock data for a given ticker and date range (e.g., /stock AAPL 2023-01-01 2023-04-30).",
        "/fundamentals": "Get fundamental data for a given stock ticker (e.g., /fundamentals aapl).",
        "/stock_analysis": "Get stock analysis for a given stock ticker (e.g., /stock_analysis AAPL).",
        "/stock_news": "Get news related to a given stock ticker (e.g., /stock_news AAPL).",
        "/market_analysis": "Get market analysis.",
        "/news": "Get news related to a given stock ticker (e.g., /news AAPL).",
        "/compare_stocks": "Compare stock performance for given tickers and date range (e.g., /compare_stocks AAPL TSLA 2023-01-29 2023-04-28).",
        "/add_stock": "Add a stock to your portfolio with a given quantity (e.g., /add_stock AAPL 40, /add_stock SBIN.BO 32).",
        "/remove_stock": "Remove a stock from your portfolio with a given quantity (e.g., /remove_stock AAPL 16).",
        "/portfolio_performance": "Get the performance of your stock portfolio.",
        "/chat": "Start a chat conversation.",
        "exit": "Exit the application."
    }

    tabs = st.tabs(["Commands", "Connect with Us", "About Us", "Reviews and Comments"])

    with tabs[0]:
        search_term = st.text_input("Search for a command", "")
        if search_term:
            search_results = [command for command, description in commands.items() if search_term.lower() in command.lower() or search_term.lower() in description.lower()]
            if search_results:
                for command in search_results:
                    st.markdown(f"**{command}**")
                    st.write(commands[command])
                    st.write("---")
            else:
                st.write("No matching commands found.")
        else:
            for command, description in commands.items():
                st.markdown(f"**{command}**")
                st.write(description)
                st.write("---")

    with tabs[1]:
        st.markdown("## Connect with Us")
        discord_link = "https://discord.gg/gHwwAWuk"
        blog_link = "https://wealth-watcher-blog.streamlit.app/"
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"Join our [Discord Channel]({discord_link})")
        with col2:
            st.markdown(f"Check out our [Blog]({blog_link})")

    with tabs[2]:
        st.markdown("## About US")
        st.write("The Wealth Watcher aims to develop an interactive, AI-powered messaging generative chatbot to assist users with various financial tasks and inquiries . It can assist with budgeting , setting financial goals, providing investment advice, answering questions about banking and credit and even helping with tax-related information.")
        st.markdown("## Our Mission")
        st.write("Our mission is to provide personal financial services of a superior quality to the users, our chief concern being their financial well-being. We desire to be the primary financial assistant for our users")
        st.markdown("## Our Vision")
        st.write("To lead financial strategy and execution, ensuring sustainable growth and long-term value for our stakeholders. My mission is to also promote transparency and collaboration across the company.")

    with tabs[3]:
#        st.markdown("## Reviews and Comments")
#        st.write("This section will display reviews and comments from users.")

        st.subheader("Email Subscription")
        email = st.text_input("Enter your email to subscribe")
        if st.button("Subscribe"):
            add_subscriber(email)

        st.subheader("Leave a Review")
        review = st.text_area("Enter your review")
        if st.button("Submit Review"):
            add_review(review)

    create_databases()

if __name__ == "__main__":
    main()
