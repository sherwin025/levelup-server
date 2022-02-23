select gr.id as gamer_id, u.first_name, u.last_name, e.description, e.date, e.time, e.game_id
from levelupapi_game g
join levelupapi_gamer gr
ON g.gamer_id = gr.id
join auth_user u
ON u.id = gr.user_id
join levelupapi_event e
ON e.organizer_id = g.gamer_id