require("dotenv").config();

const { App } = require("@slack/bolt");
console.log(process.env.SLACK_BOT_TOKEN);
// Initializes your app with your bot token and signing secret
const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  signingSecret: process.env.SLACK_SIGNING_SECRET,
  socketMode: true,
  appToken: process.env.SLACK_APP_TOKEN,
  port: process.env.PORT || 3000,
});

app.event("message", async ({ message, say }) => {
  await say(`new message from <@${message.user}>!`);
});

(async () => {
  await app.start();
  console.log("⚡️ Bolt app is running!");
})();
