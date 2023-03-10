export function parseEmail(email: string): {
  username: string;
  domain: string;
} {
  const parts = email.split("@");
  return {
    username: parts[0],
    domain: parts[1],
  };
}

export function checkOnLocal(): boolean {
  return window.location.hostname === "localhost";
}
