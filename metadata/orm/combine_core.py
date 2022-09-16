from sqlalchemy.orm import registry, relationship
from metadata.metadata_table import user_table, address_table

mapper_registry = registry()
Base = mapper_registry.generate_base()


class User(Base):
    __table__ = user_table

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User({self.name!r}, {self.fullname!r})"


class Address(Base):
    __table__ = address_table

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address({self.email_address!r})"
