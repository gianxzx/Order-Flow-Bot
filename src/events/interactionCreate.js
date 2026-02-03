import { client } from "../bot.js";
import { initClaimHandler } from "../handlers/claimHandler.js";
import { initDiscountHandler } from "../handlers/discountHandler.js";

// Initialize handlers that rely on interactions (buttons / slash commands)
export const initInteractionCreate = () => {
  initClaimHandler();
  initDiscountHandler();
};
