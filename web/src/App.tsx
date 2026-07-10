import './App.css'

const apiUrl = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'

function App() {
  return (
    <main className="app">
      <h1>GrantMatch</h1>
      <p>
        Scholarship matching, verification, and disbursement orchestration for
        African fintech integrations.
      </p>
      <p>
        <a href={`${apiUrl}/docs`} target="_blank" rel="noreferrer">
          Open API docs
        </a>
      </p>
    </main>
  )
}

export default App
