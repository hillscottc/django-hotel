## The Task
Your friend is asking to help with hotel management. Hotel is at a good location, and a lot of
reservations are made. However, life is not simple, and quite a reasonable percent of booked
reservations gets canceled. As a result, hotel sometimes has too many vacant rooms.
Your friend has a brilliant idea: implement a reservations management system that allows some
overbooking, so even if some room is reserved by someone at a specific date, other people still
can book it. 

Level of overbooking indicates number of reservations that can be booked over the hotel
capacity. Consider a hotel with 100 rooms. If level of overbooking is set to 0%, we cannot make more than 100 reservations for a specific
date. If level of overbooking is set to 10%, we can create up to 110 reservations for a specific date.

Your application has to expose 2 REST API endpoints using Python Django framework:
1. For hotel configuration, where we can set number of rooms and overbooking level.
2. For making reservations supplying
  - Guest name and email
  - Arrival and departure dates  

When max number of reservations is reached, the second endpoint responds with an error.