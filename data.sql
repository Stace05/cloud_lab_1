USE lab4;

INSERT INTO airline (airline_name, country, fleet_size) VALUES
('Windrose Airlines', 'Ukraine', 50),
('American Airlines', 'USA', 120),
('Lufthansa', 'Germany', 80);

INSERT INTO airport (airport_name, city, country) VALUES
('Boryspil International Airport', 'Kyiv', 'Ukraine'),
('John F. Kennedy International Airport', 'New York', 'USA'),
('Frankfurt Airport', 'Frankfurt', 'Germany');

INSERT INTO pilot (pilot_name, pilot_surname, license_number, total_flight_hours) VALUES
('Bohdan', 'Tynchenko', 'LIC123456', 1500),
('Wiliiam', 'Paulson', 'LIC654321', 2000),
('Stefan', 'Bauer', 'LIC112233', 1800);

INSERT INTO aircraft (airline_id, model, registration_number, total_flight_hours) VALUES
(1, 'Boeing 737', 'UA-ABC123', 5000),
(2, 'Airbus A320', 'SH-AIR456', 3000),
(3, 'Boeing 777', 'EF-EUR789', 4000);

INSERT INTO route (departure_airport_id, arrival_airport_id, distance) VALUES
(1, 2, 7500),
(2, 3, 6000),
(3, 1, 7000);

INSERT INTO flight (aircraft_id, route_id, departure_time, arrival_time, speed) VALUES
(1, 1, '2024-05-01 08:00:00', '2024-05-01 16:00:00', 850.00),
(2, 2, '2024-05-02 09:00:00', '2024-05-02 15:00:00', 830.00),
(3, 3, '2024-05-03 10:00:00', '2024-05-03 18:00:00', 900.00);

INSERT INTO crew (flight_id, pilot_id, role) VALUES
(1, 1, 'Captain'),
(1, 2, 'First Officer'),
(2, 2, 'Captain'),
(2, 3, 'First Officer'),
(3, 1, 'Captain'),
(3, 3, 'First Officer');

INSERT INTO maintenance (aircraft_id, date, details) VALUES
(1, '2024-06-01', 'Engine check'),
(2, '2024-06-15', 'Avionics update'),
(3, '2024-07-01', 'Structural inspection');

INSERT INTO registration (aircraft_id, registration_date, expiry_date) VALUES
(1, '2024-01-01', '2025-01-01'),
(2, '2024-02-01', '2025-02-01'),
(3, '2024-03-01', '2025-03-01');

INSERT INTO flighthistory (flight_id, date) VALUES
(1, '2024-05-01'),
(2,'2024-05-02'),
(3, '2024-05-03');

INSERT INTO airlineairport (airline_id, airport_id) VALUES
(1, 1), -- Windrose Airlines обслуговує Boryspil International Airport
(1, 2), -- Windrose Airlines обслуговує John F. Kennedy International Airport
(2, 2), -- American Airlines обслуговує John F. Kennedy International Airport
(2, 3), -- American Airlines обслуговує Frankfurt Airport
(3, 1), -- Lufthansa обслуговує Boryspil International Airport
(3, 3); -- Lufthansa обслуговує Frankfurt Airport

drop procedure if exists get_registrations_after_aircraft;
drop procedure if exists get_maintenances_after_aircraft;
drop procedure if exists get_aircrafts_after_airline;
drop procedure if exists get_flights_after_aircraft;
drop procedure if exists get_flighthistories_after_flight;
drop procedure if exists get_crew_after_flight;
drop procedure if exists get_crew_after_pilot;
drop procedure if exists get_airports_after_airline;
drop procedure if exists get_airlines_after_airport;

delimiter //

create procedure get_registrations_after_aircraft(
	in aircraft_id int
)
begin 
	select a.id as aircraft_id, r.id as registration_id, a.registration_number as aircraft_registration_number, 
    a.model as aircraft_model, a.total_flight_hours as aircraft_total_flight_hours
    from registration r
    join aircraft a on r.aircraft_id = a.id
    where r.aircraft_id = aircraft_id;
end //

create procedure get_maintenances_after_aircraft(
	in aircraft_id int
)
begin 
	select a.id as aircraft_id, m.id as maintenance_id, a.registration_number as aircraft_registration_number, 
    a.model as aircraft_model, a.total_flight_hours as aircraft_total_flight_hours
    from maintenance m
    join aircraft a on m.aircraft_id = a.id
    where m.aircraft_id = aircraft_id;
end //

create procedure get_aircrafts_after_airline(
	in airline_id int
)
begin 
	select al.id as airline_id, ac.id as aircraft_id, 
    al.airline_name as airline_name, 
    al.country as airline_country, al.fleet_size as airline_fleet_size
    from aircraft ac
    join airline al on ac.airline_id = al.id
    where ac.airline_id = airline_id;
end //

create procedure get_flights_after_aircraft(
	in aircraft_id int
)
begin 
	select a.id as aircraft_id, f.id as flight_id,
    a.registration_number as aircraft_registration_number, 
    a.model as aircraft_model, a.total_flight_hours as aircraft_total_flight_hours
	from flight f
	join aircraft a on f.aircraft_id = a.id
	where f.aircraft_id = aircraft_id;
end //

create procedure get_flighthistories_after_flight(
	in flight_id int
)
begin 
    select f.id as flight_id, fh.id as flighthistory_id, f.departure_time, f.arrival_time, f.speed
    from flighthistory fh
    join flight f on fh.flight_id = f.id
    where fh.flight_id = flight_id;
end //

create procedure get_crew_after_flight(
	in flight_id int
)
begin 
	select f.id as flight_id, c.id as crew_id, c.role
    from crew c
    join flight f on c.flight_id = f.id
    where c.flight_id = flight_id;
end //

create procedure get_crew_after_pilot(
	in pilot_id int
)
begin 
	select p.id as pilot_id, c.id as crew_id, p.pilot_name, p.pilot_surname, p.license_number, p.total_flight_hours
    from crew c
    join pilot p on c.pilot_id = p.id
    where c.pilot_id = pilot_id;
end //

create procedure get_airports_after_airline(
	in airline_id int
)
begin 
	select aiap.id, aiap.airline_id, ap.id as airport_id, ap.airport_name, ap.city, ap.country
	from airport ap
	join airlineairport aiap on ap.id = aiap.airport_id
	where aiap.airline_id = airline_id;
end //

create procedure get_airlines_after_airport(
	in airport_id int
)
begin 
	select aiap.id, aiap.airport_id, al.id as airline_id, al.airline_name, al.country, al.fleet_size
	from airline al
	join airlineairport aiap on al.id = aiap.airline_id
	where aiap.airport_id = airport_id;
end //