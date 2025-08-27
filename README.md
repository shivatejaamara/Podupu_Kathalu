##Podupu Kathalu 🎭##

A Streamlit-based web app for interactive Telugu riddles (పొడుపు కథలు), powered by Supabase for data storage and management.

🚀 Features

Add, manage, and solve Telugu riddles interactively.

Modern UI with Streamlit.

Data stored securely in Supabase PostgreSQL.

Easy to extend with custom riddles and pages.

🛠️ Installation
1. Clone the repository
git clone https://github.com/shivatejaamara/Podupu_Kathalu.git
cd Podupu_Kathalu

2. Create & activate a virtual environment (optional but recommended)
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Setup environment variables

Create a .env file in the project root with the following (replace with your Supabase credentials):

SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-anon-key

▶️ Running the App

Run the Streamlit app with:

streamlit run app.py


By default, it will open at:
👉 http://localhost:8501

📊 Viewing Stored Data in Supabase

Go to Supabase Dashboard
.

Select your project.

In the left menu, go to Table Editor.

Choose the riddles (or your table name) table.

Here you can:

View all stored riddles.

Edit data manually.

Run SQL queries from the SQL Editor.

📂 Project Structure
Podupu_Kathalu/
│── app.py                # Main Streamlit app
│── requirements.txt      # Python dependencies
│── insert_test_riddle.py # Script to insert test riddles
│── test_supabase.py      # Script to test Supabase connection
│── .env                  # Environment variables (ignored in Git)
│── .gitignore            # Ignore venv, .env, cache files
│── pages/                # Extra Streamlit pages
│── src/                  # Source code / utils
│── utils/                # Helper functions
│── venv/                 # Virtual environment (ignored in Git)

✅ Next Steps

Add more riddles to Supabase via the app or directly in Table Editor.

Deploy your app to Streamlit Cloud or Heroku.

Share with friends! 🎉

