import "./implementation.css";

export function SignupPanel() {
  return (
    <section className="panel">
      <h1 className="title">Join us</h1>
      <input type="email" aria-label="Email" />
      <div className="actions">
        <button className="primary" type="button">Start</button>
      </div>
    </section>
  );
}
