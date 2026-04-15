import clsx from "clsx";
import Link from "next/link";

interface MobileMenuProps {
  isOpen: boolean;
  onClose: () => void;
  menuRef: React.RefObject<HTMLDivElement | null>;
  routes: { name: string; path: string }[];
  activePathName: string;
}

export default function MobileMenu({ isOpen, onClose, menuRef, routes, activePathName }: MobileMenuProps) {
  if (!isOpen) return null;

  return (
    <div className={`${isOpen ? "block" : "hidden"} navbar`} id="navbarResponsive" ref={menuRef}>
      <ul className="navbar__list">
        {routes.map((route) => (
          <li key={route.path} className="navbar__item">
            <Link
              href={route.path}
              className={clsx("hover:text-orange", { "text-orange": activePathName === route.path }, { "text-text": activePathName !== route.path })}
            >
              {route.name}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );

  //     return (
  //     <div className="fixed inset-0 z-50 bg-black/50">
  //       <div
  //         ref={menuRef}
  //         className="fixed right-0 top-0 h-full w-64 bg-white shadow-lg p-4 transition-transform duration-300"
  //       >
  //         <button onClick={onClose} className="mb-4">✕</button>
  //         <ul>
  //           {routes.map((route) => (
  //             <li key={route.path} className="mb-3">
  //               <Link href={route.path} onClick={onClose}>
  //                 {route.name}
  //               </Link>
  //             </li>
  //           ))}
  //         </ul>
  //       </div>
  //     </div>
  //   );
}
