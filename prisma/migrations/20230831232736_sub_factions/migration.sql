-- CreateTable
CREATE TABLE `SubFaction` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` TEXT NULL,
    `holdings` VARCHAR(191) NULL,
    `user_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `FactionRanks` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` TEXT NULL,
    `rank` INTEGER NOT NULL DEFAULT 1,
    `faction_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `UnitAlleigance` (
    `id` VARCHAR(191) NOT NULL,
    `unit_id` VARCHAR(191) NOT NULL,
    `faction_id` VARCHAR(191) NOT NULL,
    `faction_rank_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `FactionRelation` (
    `id` VARCHAR(191) NOT NULL,
    `faction_id` VARCHAR(191) NOT NULL,
    `faction2_id` VARCHAR(191) NOT NULL,
    `type` ENUM('VASSAL', 'SUBJECT', 'ALLY', 'WAR') NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `SubFaction` ADD CONSTRAINT `SubFaction_user_id_fkey` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionRanks` ADD CONSTRAINT `FactionRanks_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `SubFaction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitAlleigance` ADD CONSTRAINT `UnitAlleigance_unit_id_fkey` FOREIGN KEY (`unit_id`) REFERENCES `Unit`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitAlleigance` ADD CONSTRAINT `UnitAlleigance_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `SubFaction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `UnitAlleigance` ADD CONSTRAINT `UnitAlleigance_faction_rank_id_fkey` FOREIGN KEY (`faction_rank_id`) REFERENCES `FactionRanks`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionRelation` ADD CONSTRAINT `FactionRelation_faction_id_fkey` FOREIGN KEY (`faction_id`) REFERENCES `SubFaction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `FactionRelation` ADD CONSTRAINT `FactionRelation_faction2_id_fkey` FOREIGN KEY (`faction2_id`) REFERENCES `SubFaction`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
