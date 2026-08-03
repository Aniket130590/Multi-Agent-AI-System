#from tools.tavily_tool import tavily_search
#from tools.flight_tool import search_flights
#from backend import run_travel_agent

#res = tavily_search("Best hotels in india")
#res = search_flights("plan 7 days trip nepal from bangladesh")

#test = input("Enter your travel query: ")
#res = run_travel_agent(
 #   user_input=test,
 #   thread_id='test_thread',
#)   



#print("Final response from agents:")
#print(res['answer'])

#-----------------------------------------
import asyncio
from mcp_client_test import get_all_tools , tavily_mcp_search




if __name__ == "__main__":
    query = "Latest news about AI"
    asyncio.run(tavily_mcp_search(query))

