"use client";
import { usePathname } from "next/navigation";
import clsx from "clsx";

import Link from "next/link";

import Container from "@/shared/ui/Container";
import Logo from "./Logo";

const routes = [
  { name: "Home", path: "/" },
  { name: "All News", path: "/news" },
  { name: "Incidents", path: "/incidents" },
];

export default function Header() {
  const activePathName = usePathname();

  return (
    <header className="bg-[#f7f7f7] mb-2">
      <Container>
        <div className="flex justify-between items-center py-7 font-bold">
          <Logo />
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
          <div className="md:hidden navbar" id="navbarResponsive">
            <ul className="navbar__list">
              {routes.map((route) => (
                <li key={route.path} className="navbar__item">
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
          </div>
        </div>
      </Container>
    </header>
  );
}
