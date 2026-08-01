from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

#res = tavily_search("Best hotels in india")
res = search_flights("plan 7 days trip nepal from bangladesh")

print(res)