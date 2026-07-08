const btn = document.getElementById('review-btn')
const input = document.getElementById('code-input')
const output = document.getElementById('review-output')

btn.addEventListener('click', async () => {
  const code = input.value.trim()
  if (!code) return

  btn.disabled = true
  output.textContent = 'analisando...'

  try {
    const response = await fetch('/review', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code })
    })

    const data = await response.json()
    output.textContent = data.review
  } catch (err) {
    output.textContent = 'erro ao conectar com a API.'
  } finally {
    btn.disabled = false
  }
})