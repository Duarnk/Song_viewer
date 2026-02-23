const https = require('https');

module.exports = async function handler(req, res) {
  const { tid } = req.query;
  if (!tid) return res.status(400).json({ error: 'missing tid' });

  try {
    const data = await new Promise((resolve, reject) => {
      const url = `https://open.spotify.com/oembed?url=https://open.spotify.com/track/${tid}`;
      https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, r => {
        let body = '';
        r.on('data', chunk => body += chunk);
        r.on('end', () => resolve(JSON.parse(body)));
      }).on('error', reject);
    });
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Cache-Control', 's-maxage=86400');
    return res.json(data);
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
};
