export default async function handler(req, res) {
  const { tid } = req.query;
  if (!tid) return res.status(400).json({ error: 'missing tid' });

  try {
    const url = `https://open.spotify.com/oembed?url=spotify:track:${tid}&format=json`;
    const r = await fetch(url, {
      headers: { 'User-Agent': 'Mozilla/5.0' }
    });
    if (!r.ok) return res.status(404).json({ error: 'not found' });
    const data = await r.json();
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Cache-Control', 's-maxage=86400');
    return res.status(200).json({ thumbnail_url: data.thumbnail_url });
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
}
