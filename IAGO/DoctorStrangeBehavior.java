package edu.usc.ict.iago.agent;

import java.util.ArrayList;

import edu.usc.ict.iago.utils.BehaviorPolicy;
import edu.usc.ict.iago.utils.GameSpec;
import edu.usc.ict.iago.utils.History;
import edu.usc.ict.iago.utils.Offer;

public class DoctorStrangeBehavior extends IAGOCoreBehavior implements BehaviorPolicy {
		
	// Data
	private AgentUtilsExtension utils;
	private GameSpec gameSpec;	
	private Offer allocated;
	private int adverseEvents = 0;
	
	// Constructor
	public DoctorStrangeBehavior (LedgerBehavior lb) { super(); }
	
	// Getters
	@Override
	protected Offer getAllocated () { return allocated; }
	
	@Override
	protected Offer getConceded () { return allocated; }
	
	// Setters
	@Override
	protected void setUtils(AgentUtilsExtension utils) {
		this.utils = utils;
		this.gameSpec = this.utils.getSpec();
		int numberOfIssues = this.gameSpec.getNumberIssues();
		this.allocated = new Offer(numberOfIssues);
		for(int i = 0; i < numberOfIssues; i++) {
			int[] turnInit = { 0, this.gameSpec.getIssueQuantities().get(i), 0 };
			this.allocated.setItem(i, turnInit);
		}
	}
	
	// Updates
	@Override
	protected void updateAllocated (Offer offer) { this.allocated = offer; }
	
	@Override
	protected void updateAdverseEvents (int change) { this.adverseEvents = Math.max(0, this.adverseEvents + change); }
	
	// Offer
	@Override
	protected Offer getTimingOffer(History history) { return null; }

	@Override
	protected Offer getAcceptOfferFollowup(History history) { 
		this.utils.modifyOfferLedger(1);
		return this.getNextOffer(history);
	}
	
	@Override
	protected Offer getFirstOffer(History history) { return this.getNextOffer(history); }

	@Override
	protected int getAcceptMargin() { return Math.max(0, Math.min(this.gameSpec.getNumberIssues(), this.adverseEvents)); }

	@Override
	protected Offer getRejectOfferFollowup(History history) { 
		this.utils.modifyOfferLedger(-1);
		return this.getNextOffer(history);
	}

	@Override
	protected Offer getFinalOffer(History history) {
		int numberOfIssues = this.gameSpec.getNumberIssues();
		int unclaimedItemsSum = 0;
		Offer res = new Offer(numberOfIssues);
		do {
			for(int i = 0; i < numberOfIssues; i++) unclaimedItemsSum += this.allocated.getItem(i)[1];
			res = getNextOffer(history);
			updateAllocated(res);
		} while(unclaimedItemsSum > 0);
		return res;
	}

	@Override
	public Offer getNextOffer(History history) {	
		int numberOfIssues = this.gameSpec.getNumberIssues();
		Offer res = new Offer(numberOfIssues);
		for(int i = 0; i < numberOfIssues; i++) res.setItem(i, this.allocated.getItem(i));
	
		ArrayList<Integer> playerDesires = this.utils.getMinimaxOrdering(); 
		ArrayList<Integer> AgentDesires = this.utils.getMyOrdering();
		
		int[] undecidedItems = new int[numberOfIssues];
		for(int i = 0; i < numberOfIssues; i++) 
			undecidedItems[i] = this.allocated.getItem(i)[1];
		
		int userDesiredItemIndex = -1, userSecondDesiredItemIndex = -1, agentDesiredItemIndex = -1, agentSecondDesiredItemIndex = -1;
		
		int currentHighestRank = numberOfIssues + 1;
		for(int i  = 0; i < numberOfIssues; i++)
			if(undecidedItems[i] > 0 && playerDesires.get(i) < currentHighestRank) {
				userSecondDesiredItemIndex = userDesiredItemIndex;
				userDesiredItemIndex = i;
				currentHighestRank = playerDesires.get(i);
			}
		currentHighestRank = numberOfIssues + 1;
		for(int i  = 0; i < numberOfIssues; i++)
			if(undecidedItems[i] > 0 && AgentDesires.get(i) < max) {
				agentSecondDesiredItemIndex = agentDesiredItemIndex;
				agentDesiredItemIndex = i;
				max = AgentDesires.get(i);
			}
		
		int favorStatus = this.utils.getVerbalLedger();
		if(userDesiredItemIndex == agentDesiredItemIndex) {
			int itemIndex, userItemAmount, undecidedItemAmount, agentItemAmount;
			int itemsAmount = undecidedItems[userDesiredItemIndex];

			itemIndex = userDesiredItemIndex;
			
			if (favorStatus < 0) {
				this.utils.modifyOfferLedger(-1);
				agentItemAmount = this.allocated.getItem(itemIndex)[0] + itemsAmount;
				undecidedItemAmount = 0;
				userItemAmount = this.allocated.getItem(itemIndex)[2];
				
			} else if (flavorStatue > 0) {
				if(agentSecondDesiredItemIndex !== -1) {
					this.utils.modifyOfferLedger(0);

					agentItemAmount = this.allocated.getItem(itemIndex)[0];
					undecidedItemAmount = 0;
					userItemAmount = this.allocated.getItem(itemIndex)[2] + itemsAmount;

					int tempIndex = agentSecondDesiredItemIndex;
					int tempAgentAmount = this.allocated.getItem(tempIndex)[0] + undecidedItems[tempIndex] + this.allocated.getItem(tempIndex)[2];
					res.setItem(tempIndex, tempAgentAmount, 0, 0);

				} else {
					this.utils.modifyOfferLedger(1);
					agentItemAmount = this.allocated.getItem(itemIndex)[0];
					undecidedItemAmount = itemsAmount / 2;
					userItemAmount = this.allocated.getItem(itemIndex)[2] + itemsAmount - undecidedItemAmount;
				}

			} else {
				if(itemsAmount == 2) {
					agentItemAmount = this.allocated.getItem(itemIndex)[0] + 1;
					undecidedItemAmount = 0;
					userItemAmount = this.allocated.getItem(itemIndex)[2] + 1;

				} else if (itemsAmount > 2) {
					agentItemAmount = this.allocated.getItem(itemIndex)[0] + this.allocated.getItem(itemIndex)[1] - 1;
					userItemAmount = this.allocated.getItem(itemIndex)[2] + 1;
					this.utils.modifyOfferLedger(-1);

				} else {
					agentItemAmount = this.allocated.getItem(itemIndex)[0];
					userItemAmount = this.allocated.getItem(itemIndex)[2] + 1;

					if(agentSecondDesiredItemIndex !== -1) {
						int tempIndex = agentSecondDesiredItemIndex;
						int tempAgentAmount = this.allocated.getItem(tempIndex)[0] + undecidedItems[tempIndex] + this.allocated.getItem(tempIndex)[2];
						res.setItem(tempIndex, tempAgentAmount, 0, 0);
					} else this.utils.modifyOfferLedger(1);
				}
			}

			res.setItem(itemIndex, new int [] { agentItemAmount, undecidedItemAmount, userItemAmount });
			return res;
		}
		
		int[] userState = new int[3];
		int[] agentState = new int[3];

		if (favorStatus < 0) {
			this.utils.modifyOfferLedger(-1);
			agentState[0] = this.allocated.getItem(agentDesiredItemIndex)[0] + undecidedItems[agentDesiredItemIndex] + this.allocated.getItem(agentDesiredItemIndex)[2];
			agentState[1] = 0;
			agentState[2] = 0;
			res.setItem(agentDesiredItemIndex, agentState);

			if(userSecondDesiredItemIndex !== agentDesiredItemIndex) {
				userState[0] = this.allocated.getItem(userSecondDesiredItemIndex)[0];
				userState[1] = 0;
				userState[2] = this.allocated.getItem(userSecondDesiredItemIndex)[2] + undecidedItems[userSecondDesiredItemIndex];
				res.setItem(userSecondDesiredItemIndex, userState);
			}

		} else if (favorStatus > 0) {
			this.utils.modifyOfferLedger(1);
			userState[0] = this.allocated.getItem(userDesiredItemIndex)[0];
			userState[1] = 0;
			userState[2] = undecidedItems[userDesiredItemIndex] + this.allocated.getItem(userDesiredItemIndex)[2];
			res.setItem(userDesiredItemIndex, userState);

			agentState[1] = undecidedItems[agentDesiredItemIndex] / 2;
			agentState[0] = this.allocated.getItem(agentDesiredItemIndex)[0] + this.allocated.getItem(agentDesiredItemIndex)[1] - agentState[1];
			agentState[2] = this.allocated.getItem(agentDesiredItemIndex)[2];
			res.setItem(agentDesiredItemIndex, agentState);
	
		} else {
			userState[0] = this.allocated.getItem(userDesiredItemIndex)[0];
			userState[1] = 0;
			userState[2] = undecidedItems[userDesiredItemIndex] + this.allocated.getItem(userDesiredItemIndex)[2];
			res.setItem(userDesiredItemIndex, userState);

			agentState[0] = this.allocated.getItem(agentDesiredItemIndex)[0] + undecidedItems[agentDesiredItemIndex];
			agentState[1] = 0;
			agentState[2] = this.allocated.getItem(agentDesiredItemIndex)[2];
			res.setItem(agentDesiredItemIndex, agentState);
		}

		return res;
	}
}
