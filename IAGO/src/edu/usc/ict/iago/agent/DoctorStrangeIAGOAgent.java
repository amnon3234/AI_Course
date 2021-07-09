package edu.usc.ict.iago.agent;

import javax.websocket.Session;

import edu.usc.ict.iago.utils.GameSpec;

public class DoctorStrangeIAGOAgent extends IAGOCoreVH {

    // Constructor
    public DoctorStrangeIAGOAgent(String name, GameSpec game, Session session) {
        super("DoctorStrangeIAGOAgent", game, session, new DoctorStrangeBehavior(), new DoctorStrangeExpression(), new DoctorStrangeMessage(game));
        super.safeForMultiAgent = true;
    }

    @Override
    public String getArtName() { return "DoctorStrangeIAGOAgent"; }

    @Override
    public String agentDescription() { return "<h1>Doctor Strange</h1><p> is excited to begin negotiating!</p>"; }
}