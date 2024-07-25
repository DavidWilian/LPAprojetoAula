from Code.EnemyShot import EnemyShot
from Code.Entity import Entity
from Code.PlayerShot import PlayerShot
from Code.const import WIN_WIDTH


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):  # Quando é colocado os dois underlines a função não pode ser usada fora da classe
        if isinstance(ent, Entity):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
