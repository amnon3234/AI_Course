package edu.usc.ict.iago.agent;

import edu.usc.ict.iago.utils.Event;
import edu.usc.ict.iago.utils.ExpressionPolicy;
import edu.usc.ict.iago.utils.History;

public class DoctorStrangeExpression extends IAGOCoreExpression implements ExpressionPolicy {

    protected String getSemiFairEmotion() {
        return "neutral";
    }

    protected String getFairEmotion() {
        return "happy";
    }

    protected String getUnfairEmotion() {
        return "angry";
    }

    @Override
    public String getExpression(History history) {
        Event userEvent = history.getUserHistory().getLast();
        if (userEvent.getType().equals(Event.EventClass.SEND_MESSAGE)) {
            Event.SubClass type = userEvent.getSubClass();
            switch (type) {
                case BATNA_INFO:
                    return "happy";
                case CONFUSION:
                    return "sad";
                case FAVOR_ACCEPT:
                    return "happy";
                case FAVOR_REJECT:
                    return "angry";
                case FAVOR_REQUEST:
                    return "neutral";
                case FAVOR_RETURN:
                    return "happy";
                case GENERIC_NEG:
                    return "sad";
                case GENERIC_POS:
                    return "surprised";
                case OFFER_ACCEPT:
                    return "happy";
                case OFFER_REJECT:
                    return "angry";
                case OFFER_REQUEST_NEG:
                    return "sad";
                case OFFER_REQUEST_POS:
                    return "happy";
                case PREF_INFO:
                    return "happy";
                case PREF_WITHHOLD:
                    return "neutral";
                case THREAT_NEG:
                    return "sad";
                case THREAT_POS:
                    return "neutral";
                default:
                    return null;
            }
        } else if (userEvent.getType().equals(Event.EventClass.FORMAL_ACCEPT) {
            return "happy";
        }
        else{
            return null;
        }
    }
}
