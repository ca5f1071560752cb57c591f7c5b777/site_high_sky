DROP FUNCTION public.arrival_count(integer, integer);

CREATE FUNCTION public.arrival_count(IN outer_airliner_id integer, IN outer_airport_id integer) RETURNS bigint AS
$BODY$DECLARE
    qty int;
BEGIN
select sum(airlines_schedulerecord.per_day)
	into qty
	from airlines_airport, airlines_schedulerecord, airlines_flight, airlines_airliner_routes, airlines_airliner 
	where outer_airport_id = airlines_airport.id 
		and airlines_airport.id = airlines_flight.arrival_id 
		and airlines_flight.route_id = airlines_airliner_routes.route_id
		and airlines_flight.route_id = airlines_schedulerecord.route_id
		and airlines_airliner_routes.airliner_id = airlines_airliner.id 
		and airlines_airliner.id = outer_airliner_id;
	return qty;
END;
$BODY$
LANGUAGE plpgsql VOLATILE NOT LEAKPROOF;

