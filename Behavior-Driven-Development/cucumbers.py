from dataclasses import dataclass, field

@dataclass
class CucumberBasket:
    count: int = 0
    max_count: int | None = None
    _history: list[tuple[str, int]] = field(default_factory=list)

    def add(self, n: int) -> None:
        n = int(n)
        if n < 0:
            raise ValueError("Cannot add negative cucumbers")
        if self.max_count is not None and self.count + n > self.max_count:
            raise ValueError("Exceeds capacity")
        self.count += n
        self._history.append(("add", n))

    def remove(self, n: int) -> None:
        n = int(n)
        if n < 0:
            raise ValueError("Cannot remove negative cucumbers")
        if n > self.count:
            raise ValueError("Not enough cucumbers")
        self.count -= n
        self._history.append(("remove", n))

    def clear(self) -> None:
        if self.count > 0:
            removed = self.count
            self.count = 0
            self._history.append(("clear", removed))

    def is_empty(self) -> bool:
        return self.count == 0
    
    def add_up_to(self, n: int) -> int:
        n = int(n)
        if n <= 0:
            return 0

        if self.max_count is None:
            self.count += n
            self._history.append(("add_up_to", n))
            return n

        remaining = self.max_count - self.count
        to_add = min(n, remaining)
        if to_add > 0:
            self.count += to_add
            self._history.append(("add_up_to", to_add))
        return to_add
    
    def remove_up_to(self, n: int) -> int:
        n = int(n)
        if n <= 0:
            return 0
        to_remove = min(n, self.count)
        if to_remove > 0:
            self.count -= to_remove
            self._history.append(("remove_up_to", to_remove))
        return to_remove
