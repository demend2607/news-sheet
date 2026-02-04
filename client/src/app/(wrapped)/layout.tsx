import Container from "@/shared/ui/Container";

export default function WrappedLayout({ children }: { children: React.ReactNode }) {
  return <Container>{children}</Container>;
}
