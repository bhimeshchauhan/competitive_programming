# Reservation and Payments System for Parking Garage

---
---

## Functional Requirements

- The system must be able to reserve a parking spot for a vehicle.
- The system must be able to pay for a parking spot.
- The system must be able to cancel a reservation.
- The system must be able to display the status of the parking garage.
- Three types of vehicles are supported:
  - Car
  - Motorcycle
  - Bus
- Prices for each vehicle type are as follows:
  - Car: $5
  - Motorcycle: $2
  - Bus: $10
- Prices are per hour.

## Interface

- Public Endpoints
  - /reserve
    - Method: POST
    - Request Body:
      - vehicleType: string
      - startTime: string
      - endTime: string
      - garageId: string
  - /pay
    - Method: POST
    - Request Body:
      - vehicleId: string
      - bookingId: string
      - paymentType: string
      - paymentAmount: number
      - paymentCurrency: string
  - /cancel
    - Method: POST
    - Request Body:
      - bookingId: string
  - /status
    - Method: GET
    - Request Body:
      - garageId: string

- Internal Endpoints
  - /calculatePrice
    - Method: POST
    - Request Body:
      - vehicleType: string
      - startTime: string
      - endTime: string
      - garageId: string
    - /reserveSpot
      - Method: POST
      - Request Body:
        - vehicleType: string
        - startTime: string
        - endTime: string
        - garageId: string
    - /cancelSpot
      - Method: POST
      - Request Body:
        - bookingId: string
    - /getSpotStatus
      - Method: GET
      - Request Body:
        - garageId: string
    - /getSpotPrice
      - Method: GET
      - Request Body:
        - garageId: string


## Data Model

```
PAYMENT:
    - paymentId: string
    - paymentType: string
    - paymentAmount: number
    - paymentCurrency: string
    - paymentStatus: string
    - paymentTime: string
    - paymentMethod: string

GARAGE:
    - garageId: string
    - name: string
    - address: string
    - location: string
    - capacity: number
    - availableSpots: number
    - vehicleTypes: [string]
    - spotPrices: {
        - vehicleType: number
    }
VEHICLE:
    - vehicleId: string
    - vehicleType: string
    - bookingId: string
    - garageId: string
    - startTime: string
    - endTime: string
    - payment: PAYMENT

BOOKING:
    - bookingId: string
    - vehicleId: string
    - garageId: string
    - startTime: string
    - endTime: string
    - payment: PAYMENT

AUTH:
    - userId: string
    - userName: string
    - userEmail: string
    - userPassword: string

DATABASE CHOICE
    - PostgreSQL
```