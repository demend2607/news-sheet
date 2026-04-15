"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

import clsx from "clsx";
import { HamburgerMenuIcon, CrossCircledIcon } from "@radix-ui/react-icons";

import Container from "@/shared/ui/Container";
import Logo from "./Logo";
import MobileMenu from "./MobileMenu";
import useMobileMenu from "@/shared/lib/hooks/useMobileMenu";

const routes = [
  { name: "Home", path: "/" },
  { name: "All News", path: "/news" },
  { name: "Incidents", path: "/incidents" },
];

export default function Header() {
  const activePathName = usePathname();

  const { isOpen, toggle, close, menuRef } = useMobileMenu();

  return (
    <header className="bg-[#f7f7f7] mb-2">
      <Container>
        <div className="flex justify-between items-center py-7 font-bold">
          <Logo />
          <div className="md:hidden menu_drop" aria-label="Menu">
            {isOpen ? <CrossCircledIcon onClick={close} /> : <HamburgerMenuIcon onClick={toggle} />}
          </div>
          <nav className="h-full hidden md:flex  items-center text-xl ">
            <ul className="flex gap-8 ">
              {routes.map((route) => (
                <li key={route.path}>
                  <Link
                    href={route.path}
                    className={clsx(
                      "hover:text-orange",
                      { "text-orange": activePathName === route.path },
                      { "text-text": activePathName !== route.path },
                    )}
                  >
                    {route.name}
                  </Link>
                </li>
              ))}
            </ul>
          </nav>
          <MobileMenu isOpen={isOpen} onClose={close} menuRef={menuRef} activePathName={activePathName} routes={routes} />
        </div>
      </Container>
    </header>
  );
}
