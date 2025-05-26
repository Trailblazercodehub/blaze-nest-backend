Booking API Documentation
Base URL
https://api.blazenest.com/api/v1/

Authentication
JWT Token required for all endpoints

Include in headers:

Authorization: Bearer <your_token>
Endpoints
1. Create a Booking
POST /bookings/

Request Body:

json
{
  "accommodation_id": "integer (required)",
  "check_in": "YYYY-MM-DD (required)",
  "check_out": "YYYY-MM-DD (required)",
  "guests": "integer (required)",
  "special_requests": "string (optional)"
}
Success Response (201 Created):

json
{
  "id": "integer",
  "user": "user_id",
  "accommodation": {
    "id": "integer",
    "name": "string",
    "price_per_night": "decimal"
  },
  "total_amount": "decimal",
  "status": "confirmed",
  "created_at": "datetime"
}
2. List User Bookings
GET /bookings/

Query Params:

?status=confirmed (Filter by status)

?ordering=-created_at (Sort by newest first)

Success Response (200 OK):

json
[
  {
    "id": 1,
    "accommodation_name": "Luxury Villa",
    "check_in": "2023-12-15",
    "total_amount": 1200.00,
    "status": "confirmed"
  }
]
3. Booking Details
GET /bookings/{id}/

Success Response (200 OK):

json
{
  "id": 1,
  "accommodation": {
    "id": 5,
    "name": "Beachfront Suite",
    "amenities": ["WiFi", "Pool"]
  },
  "payment_status": "paid",
  "cancellation_policy": "Free cancellation within 48h"
}
4. Cancel Booking
PATCH /bookings/{id}/cancel/

Success Response (200 OK):

json
{
  "message": "Booking cancelled",
  "refund_amount": 950.00
}
5. Availability Check
GET /bookings/availability/

Query Params:

?accommodation_id=1

?check_in=2023-12-20

?check_out=2023-12-25

Response (200 OK):

json
{
  "available": true,
  "total_price": 1500.00
}
Error Responses
Code	Error	Description
400	Invalid dates	Check-out before check-in
403	Forbidden	Not your booking
404	Not found	Booking doesn't exist
409	Conflict	Dates already booked
