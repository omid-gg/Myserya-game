app.post('/7869614206:AAFKyhtNjeb_nRM883nnrPoROScjkSNtUfc', async (req, res) => {
    const { message } = req.body;
    if (message) {
        const chatId = message.chat.id;
        const text = message.text;

        await fetch(`https://api.telegram.org/bot7869614206:AAFKyhtNjeb_nRM883nnrPoROScjkSNtUfc/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ chat_id: chatId, text: 'ربات فعال است!' })
        });

        res.send('OK');
    } else {
        res.send('No message found.');
    }
});
