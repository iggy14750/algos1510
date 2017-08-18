

 5. **100 Prisoners**
    One prisoner is elected to be the decider, the one who keeps count. When anyone - other than the decider - enters the room, he observes whether the light is on. If it is, leave it on for the next person. If it is not, then we ask whether a prisoner has turned the light on before (not simply left it on). If he has, he leaves the light off. If he has not, he turns it on for the next to see.
    
    When the decider enters the room, he observes whether the light has been left on. If it has, he adds one to his tally (which began at 1 with himself). He turns it off after noticing it. If the light is off, he leaves it off, and does not add one to his tally. When his tally finally reaches 100, he can confidently say that all 100 prisoners had turned the light on and therefore been in the room, and can call for their release.
    
    ```
    def enter_room(prisoner):
        if prisoner.is_decider:
            if light.is_on:
                prisoner.tally += 1
            if prisoner.tally == 100:
                call_for_release()
        elif not light.is_on and not prisoner.has_turned_light_on:
            light.is_on = True
            prisoner.has_turned_light_on = True
    ```