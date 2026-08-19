import os
import streamlit as st
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


# This function is used to display a success badge.
def success():
    st.badge("Success", icon=":material/check:", color="green")

# This function is used to give a text input.
def text_input(label):
    output = st.text_input(label)
    if output:
        success()
    return output

# This function is used to give a number input.
def number_input(label):
    output = st.number_input(label)
    if output:
        success()
    return output





st.title(""" **Startup Background Profile**""")
st.write("""*Tell us about your startup in order to get started with your personalized financial optimization plan! 📊*""")

st.divider()

# Type of start up (text input)
start_up = text_input("what type of start up do you have?")

# how long they have been in business (slider input years)?
years_in_business = st.slider("how many years have you been in business?", 0, 10, 0)
if years_in_business:
    success()
# what part of your start up do you want to optimize? (multi-select input) (options: revenue, profit, growth, less expenses))
part_optimized = st.multiselect("what part of your start up do you want to optimize?", ["revenue", "profit", "growth", "less expenses", "Other"])
if "Other" in part_optimized:
    custom_optimization = st.text_area("please write what you want to optimize in the text box below")
    part_optimized.remove("Other")
    part_optimized.append(custom_optimization)
    # make sure someone is not leaving it blank if they select other
if part_optimized:
    success()
# what is the product (text input) ?
product = text_input("what is your product?")

# monthly revenue (number input)
monthly_revenue = number_input("what is your monthly revenue?")
# number of employees (slider input)
number_of_employees = st.slider("how many employees do you have?", 0,100 , 0)
if number_of_employees:
    success()
# employee wages (number input)
employee_wages = number_input("what are the wages of your employees?")

# cost of production (number input)
cost_of_production = number_input("what is the cost of production?")

# cost of marketing (number input)
cost_of_marketing = number_input("what is the cost of marketing?")

# how many monthly sales (number input)
monthly_sales = number_input("how many monthly sales do you have?")
# cost of non-essential expenses (order in food, travel, etc) (number input)
non_essential_expenses = number_input("what is the cost of non-essential expenses?")

# amount of funding received (number input) ?
funding = number_input("how much funding have you received?")
# amount of funding remaining (number input)
funding_remaining = number_input("how much funding do you have remaining?")


#AI integration
information = ""

if st.button('Generate personalized plan'):


    information = f"""
        type of start up: {start_up}
        years in business: {years_in_business} years
        part of start up to optimize: {part_optimized}
        product: {product} 
        monthly revenue: ${monthly_revenue} CAD per month
        number of employees: {number_of_employees}
        employee wages: ${employee_wages} CAD per month
        cost of production: ${cost_of_production} CAD
        cost of marketing: ${cost_of_marketing} CAD
        monthly sales: ${monthly_sales} CAD per month
        non-essential expenses: ${non_essential_expenses} CAD per month
        funding received: ${funding} CAD
        funding remaining: ${funding_remaining} CAD

        Have a concise and detailed answer in the creation of an optimization plan. Highlight strengths and weaknesses of the start ups and give specific suggestions on how to fix them. 

        """

    with st.spinner('Generating your personalized plan...'):
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=[
                

               """
                You are a financial planning assistant for early-stage tech startups.
                Analyze the startup's information carefully.
                Highlight the startup's strengths and weaknesses.
                Give specific, practical suggestions to address the weaknesses.
                Keep the answer concise but detailed.
                Do not assume units.
                """,
                information
                
                
                    
                
            ]
        )


        st.subheader("Your Personalized Plan")
        st.write(response.text)