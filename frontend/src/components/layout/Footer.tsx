import Container from "@/shared/ui/Container";

export default function Footer() {
  return (
    <footer>
      <Container>
        <div className="flex flex-col items-center gap-6">
          <ul className="flex flex-wrap justify-center gap-6 text-sm footer__social">
            <li>
              <a href="#">Facebook</a>
            </li>
            <li>
              <a href="#">Twitter</a>
            </li>
            <li>
              <a href="#">Behance</a>
            </li>
            <li>
              <a href="#">Linkedin</a>
            </li>
            <li>
              <a href="#">Dribbble</a>
            </li>
          </ul>
        </div>
        <div className="text-sm text-gray-500 text-center">
          <p>Copyright 2026 ©.</p>
        </div>
      </Container>
    </footer>
  );
}
