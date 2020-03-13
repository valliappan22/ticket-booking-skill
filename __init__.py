from mycroft import MycroftSkill, intent_file_handler


class TicketBooking(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('booking.ticket.intent')
    def handle_booking_ticket(self, message):
        self.speak_dialog('booking.ticket')


def create_skill():
    return TicketBooking()

