class MessagesTwitter(object):

    def get_message_making_coffee(self):
        return "%02d:%02d começando os preparativos para um café. ThoughtWorks"

    def get_message_abort(self):
        msg = "As %02d:%02d deu treta na cafeteira,voltamos em alguns minutos!"
        return msg
