import { initCloseHandler } from "../handlers/closeHandler.js";
import { initWebhookHandler } from "../handlers/webhookHandler.js";

// Initialize handlers that rely on messageCreate
export const initMessageCreate = () => {
  initCloseHandler();
  initWebhookHandler();
};
