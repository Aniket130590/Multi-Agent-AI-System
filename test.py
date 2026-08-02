from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

#res = tavily_search("Best hotels in india")
#res = search_flights("plan 7 days trip nepal from bangladesh")

test = input("Enter your travel query: ")
res = run_travel_agent(
    user_input=test,
    thread_id='test_thread',
)   



print("Final response from agents:")
print(res['answer'])