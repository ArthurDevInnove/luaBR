export function getCookie(cookieName) {
  let name = cookieName + "=";
  let decodedCookie = decodeURIComponent(document.cookie);

  let splitedCookie = decodedCookie.split(";");

  for (let i = 0; i < splitedCookie.length; i++) {
    let cookieCharacter = splitedCookie[i];

    while (cookieCharacter.charAt(0) == " ") {
      cookieCharacter.substring(1);
    }

    if (cookieCharacter.indexOf(name) == 0) {
      return cookieCharacter.substring(name.length, cookieCharacter.length);
    }
  }

  return "";
}
